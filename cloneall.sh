GHORG=eventbrite;
for page in $(seq 1 20); do curl "https://api.github.com/orgs/$GHORG/repos?access_token=339f6c8dd006632ccd35060d73ffe10ba93341d7&per_page=2000&page="+$page | grep -o 'git@[^"]*' | xargs -L1 git clone; done
# for page in $(seq 1 20); do curl "https://api.github.com/orgs/$GHORG/repos?access_token=339f6c8dd006632ccd35060d73ffe10ba93341d7&per_page=2000&page="+$page | grep -o 'git@[^"]*service' | xargs -L1 git clone; done

