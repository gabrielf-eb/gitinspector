#!/bin/sh
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8


inspect_repo_monthly() {
    month="01"
    inspect_repo_monthly_month
    month="02"
    inspect_repo_monthly_month
    month="03"
    inspect_repo_monthly_month
    # month="04"
    # inspect_repo_monthly_month
    # month="05"
    # inspect_repo_monthly_month
    # month="06"
    # inspect_repo_monthly_month
    # month="07"
    # inspect_repo_monthly_month
    # month="08"
    # inspect_repo_monthly_month
    # month="09"
    # inspect_repo_monthly_month
    # month="10"
    # inspect_repo_monthly_month
    # month="11"
    # inspect_repo_monthly_month
    # month="12"
    # inspect_repo_monthly_month
}

inspect_repo_monthly_month() {
    echo "Processing $repo $year-$month"
    # file="./output/commit_info_"
    # file+="$repo"
    # file+="_"
    # file+="$year"
    # file+="_"
    # file+="$month"
    # file+=".sql"
    # echo "INSERT INTO hive.team_comms_eng.eb_commits values " > "$file"
    python gitinspector.py -F html -r -T -w --since=$year-$month-01 --until=$year-$month-31  /Users/gabrielf/eventbrite/$repo
}

inspect_repo_yearly() {
    echo "Processing $repo $year"
    # file="./output/commit_info_"
    # file+="$repo"
    # file+="_"
    # file+="$year"
    # file+=".sql"
    # echo "INSERT INTO hive.team_comms_eng.eb_commits values " > "$file"
    python gitinspector.py -F html -r -T -w --since=$year-01-01 --until=$year-12-31  /Users/gabrielf/eventbrite/$repo
    # python gitinspector.py -F html -r -T -w --since=$year-01-01 --until=$year-04-30  /Users/gabrielf/eventbrite/$repo
}

year=2020
# year=2020


repo="order_service"
inspect_repo_yearly

repo="core"
inspect_repo_yearly

# repo="distribution_service"
# inspect_repo_yearly

# repo="inventory_service"
# inspect_repo_yearly

# repo="journal_service"
# inspect_repo_yearly

# repo="message_service"
# inspect_repo_yearly

# repo="auth_service"
# inspect_repo_yearly

# repo="survey_service"
# inspect_repo_yearly

# repo="billing_service"
# inspect_repo_yearly

# repo="tag_service"
# inspect_repo_yearly

# repo="cerberus_service"
# inspect_repo_yearly

# repo="payment_service"
# inspect_repo_yearly

# repo="event_service"
# inspect_repo_yearly

# repo="ticket_availability_service"
# inspect_repo_yearly

# repo="destination_service"
# inspect_repo_yearly

# repo="pricing_service"
# inspect_repo_yearly

# repo="user_service"
# inspect_repo_yearly

# repo="search_service"
# inspect_repo_yearly



# repo="app_marketplace_service"
# inspect_repo_yearly

# repo="missive_service"
# inspect_repo_yearly

# repo="spa_deployment_service"
# inspect_repo_yearly

# repo="artist_service"
# inspect_repo_yearly

# repo="example_service"
# inspect_repo_yearly

# repo="moments_service"
# inspect_repo_yearly

# repo="sponsor_service"
# inspect_repo_yearly

# repo="asset_service"
# inspect_repo_yearly

# repo="external_aggregation_service"
# inspect_repo_yearly

# repo="newsletter_service"
# inspect_repo_yearly

# repo="structured_content_service"
# inspect_repo_yearly

# repo="assortments_service"
# inspect_repo_yearly

# repo="fulfillment_service"
# inspect_repo_yearly

# repo="nexus_service"
# inspect_repo_yearly

# repo="attendee_service"
# inspect_repo_yearly

# repo="geo_service"
# inspect_repo_yearly

# repo="guestlist_service"
# inspect_repo_yearly

# repo="organizer_service"
# inspect_repo_yearly

# repo="tax_service"
# inspect_repo_yearly

# repo="image_service"
# inspect_repo_yearly

# repo="payment_capability_service"
# inspect_repo_yearly

# repo="theme_builder_service"
# inspect_repo_yearly

# repo="booking_service"
# inspect_repo_yearly

# repo="insights_service"
# inspect_repo_yearly

# repo="ticket_availability_service"
# inspect_repo_yearly

# repo="bookmark_service"
# inspect_repo_yearly

# repo="internal_aggregation_service"
# inspect_repo_yearly

# repo="ugc_service"
# inspect_repo_yearly

# repo="recommender_service"
# inspect_repo_yearly

# repo="commentary_service"
# inspect_repo_yearly

# repo="refund_service"
# inspect_repo_yearly

# repo="venue_service"
# inspect_repo_yearly

# repo="connect_marketplace_service"
# inspect_repo_yearly

# repo="logistics_service"
# inspect_repo_yearly

# repo="report_service"
# inspect_repo_yearly

# repo="waiting_room_service"
# inspect_repo_yearly

# repo="merchandise_service"
# inspect_repo_yearly

# repo="webhooks_service"
# inspect_repo_yearly

# repo="soa_proxy_service"
# inspect_repo_yearly


# repo="payment_capability_service"
# inspect_repo_yearly


# https://admin.eventbrite.com/admin/spa/

# repo="nearme_web"
# inspect_repo_yearly

# repo="destination_tools"
# inspect_repo_yearly

# repo="checkout_spa"
# inspect_repo_yearly

# repo="react-venue-map"
# inspect_repo_yearly

# repo="xdev-docs"
# inspect_repo_yearly

# repo="feed_web"
# inspect_repo_yearly

# repo="app_marketplace_spa"
# inspect_repo_yearly


# repo="core"
# # inspect_repo_monthly
# inspect_repo_yearly

# Libs

# repo="yak-configs"
# inspect_repo_yearly

# repo="yak"
# inspect_repo_yearly

# repo="docker-dev"
# inspect_repo_yearly

# repo="eventbrite_api"
# inspect_repo_yearly

# repo="soa"
# inspect_repo_yearly

# repo="soa_proxy_service"
# inspect_repo_yearly

# repo="ebsoa"
# inspect_repo_yearly

# repo="pysoa"
# inspect_repo_yearly
