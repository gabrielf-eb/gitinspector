import os
import csv
from datetime import datetime, timedelta

from pyhive import presto

from gitinspector.gitinspector import execute


def get_presto():
    connection = presto.connect(
        'presto-tableau.prod.dataf.eb',
        8443,
        'gabrielf',
        password='Zxcvbnm123$',
        protocol='https',
    )
    return connection.cursor()


def presto_get_repos():
    # c
    # cursor.execute('INSERT INTO hive.team_comms_eng.eb_commits_repos values (61, \'legacy_search_service\', \'service\', \'TRUE\', \'SOA\')')
    # print(cursor.fetchall())
    # cursor.execute('Select * from team_comms_eng.eb_commits_repos')
    cursor = get_presto()
    cursor.execute('SELECT repo, MAX(date) FROM team_comms_eng.eb_commits GROUP BY repo')
    return cursor.fetchall()


def presto_execute(sql):
    cursor = get_presto()
    cursor.execute(sql)
    print(cursor.fetchall())


def get_all_repos():
    repos = []
    for element in os.listdir('/Users/gabrielf/eventbrite'):
        directory = os.path.join('/Users/gabrielf/eventbrite', element)
        if os.path.isdir(directory):
            repos.append(element)
    return repos


def process():
    repos = get_all_repos()
    last_executions = presto_get_repos()
    last_executions_index = {
        repo: str_last_date_commit for repo, str_last_date_commit in last_executions
    }
    for repo in repos:
        if repo not in last_executions_index:
            last_executions_index[repo] = '2000-01-01'
    for repo, str_last_date_commit in last_executions_index.items():
        last_date_commit = datetime.strptime(str_last_date_commit, '%Y-%m-%d')
        from_date_commit = last_date_commit + timedelta(days=1)
        print(repo, str_last_date_commit, last_date_commit, from_date_commit)
        today = datetime.now()
        from_day = from_date_commit.day
        from_month = from_date_commit.month
        # year complete
        for from_year in range(from_date_commit.year, today.year + 1):
            from_date = '{}-{}-{}'.format(
                from_year,
                str(from_month).zfill(2),
                str(from_day).zfill(2),
            )
            if from_year == today.year:
                yesterday = today - timedelta(days=1)
                to_date = '{}-{}-{}'.format(
                    from_year,
                    str(yesterday.month).zfill(2),
                    str(yesterday.day).zfill(2),
                )
            else:
                to_date = '{}-12-31'.format(from_year)
            repository = '/Users/gabrielf/eventbrite/{}'.format(repo)
            if os.path.isdir(repository):
                try:
                    inserts = execute(
                        repository,
                        from_date,
                        to_date,
                    )
                    page_size = 500
                    print(repo, from_date, to_date)
                    for insert_page in range(0, len(inserts), page_size):
                        print('Inserting {} {} {}'.format(repo, insert_page, insert_page + page_size))
                        sql = ', '.join(inserts[insert_page:insert_page + page_size])
                        presto_execute('INSERT INTO hive.team_comms_eng.eb_commits VALUES {}'.format(sql))
                except Exception as e:
                    print(e)
            from_day = 1
            from_month = 1


def update_unknown_repos():
    cursor = get_presto()
    cursor.execute(
        'SELECT commit.repo '
        'FROM team_comms_eng.eb_commits commit WHERE commit.repo not in (SELECT repo FROM team_comms_eng.eb_commits_repos repo) '
        'GROUP BY commit.repo'
    )
    unknown_repos = cursor.fetchall()
    cursor.execute('SELECT MAX(id) from team_comms_eng.eb_commits_repos')
    last_repo_id = cursor.fetchall()[0][0]
    inserts = []
    for unknown_repo in unknown_repos:
        last_repo_id += 1
        sql = (
            "("
            "{}, "
            "'{}', "
            "'{}', "
            "'{}', "
            "'{}' "
            ") "
        )
        inserts.append(
            sql.format(
                last_repo_id,
                unknown_repo[0],
                'service' if 'service' in unknown_repo[0] else 'library',
                'TRUE' if 'service' in unknown_repo[0] else 'FALSE',
                'PYSOA' if 'service' in unknown_repo[0] else 'LIB',
            )
        )
    page_size = 500
    for insert_page in range(0, len(inserts), page_size):
        print('Inserting unknown_repos {} {}'.format(insert_page, insert_page + page_size))
        sql = ', '.join(inserts[insert_page:insert_page + page_size])
        presto_execute('INSERT INTO hive.team_comms_eng.eb_commits_repos VALUES {}'.format(sql))


def update_unknown_authors():
    cursor = get_presto()
    cursor.execute(
        'SELECT commit.email, commit.author, MAX(commit.date) '
        'FROM team_comms_eng.eb_commits commit WHERE commit.email not in (SELECT email FROM team_comms_eng.eb_commits_author author) '
        'GROUP BY commit.email, commit.author'
    )
    unknown_authors = cursor.fetchall()
    cursor.execute('SELECT MAX(id) from team_comms_eng.eb_commits_author')
    last_author_id = cursor.fetchall()[0][0]
    inserts = []
    for unknown_author in unknown_authors:
        last_author_id += 1
        sql = (
            "("
            "{}, "
            "'{}', "
            "'{}', "
            "'', "
            "'', "
            "'' "
            ") "
        )
        inserts.append(
            sql.format(
                last_author_id,
                unknown_author[1],
                unknown_author[0],
            )
        )
    page_size = 500
    for insert_page in range(0, len(inserts), page_size):
        print('Inserting unknown_authors {} {}'.format(insert_page, insert_page + page_size))
        sql = ', '.join(inserts[insert_page:insert_page + page_size])
        presto_execute('INSERT INTO hive.team_comms_eng.eb_commits_author VALUES {}'.format(sql))


def update_all_engs():
    try:
        presto_execute('DROP TABLE hive.team_comms_eng.eb_commits_author_2')
    except Exception as e:
        pass
    presto_execute(
        'CREATE TABLE hive.team_comms_eng.eb_commits_author_2 ('
        ' id INTEGER, '
        ' briteling VARCHAR(255), '
        ' email VARCHAR(255), '
        ' location VARCHAR(255), '
        ' team VARCHAR(255), '
        ' bu VARCHAR(255) '
        ')'
    )
    with open('all_engs_updated2.csv') as f:
        reader = csv.reader(f)
        inserts = []
        last_author_id = 0
        for row in reader:
            print(row)
            last_author_id += 1
            sql = (
                "("
                "{}, "
                "'{}', "
                "'{}', "
                "'{}', "
                "'{}', "
                "'{}' "
                ") "
            )
            inserts.append(
                sql.format(
                    last_author_id,
                    row[1],
                    row[2],
                    row[5],
                    row[6],
                    row[7],
                )
            )
    page_size = 500
    for insert_page in range(0, len(inserts), page_size):
        print('Inserting authors {} {}'.format(insert_page, insert_page + page_size))
        sql = ', '.join(inserts[insert_page:insert_page + page_size])
        presto_execute('INSERT INTO hive.team_comms_eng.eb_commits_author_2 VALUES {}'.format(sql))

    presto_execute('ALTER TABLE hive.team_comms_eng.eb_commits_author RENAME TO hive.team_comms_eng.eb_commits_author_bak')
    presto_execute('ALTER TABLE hive.team_comms_eng.eb_commits_author_2 RENAME TO hive.team_comms_eng.eb_commits_author')


if __name__ == '__main__':
    process()
    update_unknown_authors()
    update_unknown_repos()
    # update_all_engs()
