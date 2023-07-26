def list_account_dashboards(qs_client, account_id, aws_region):

    response_dashboard = qs_client.list_dashboards(AwsAccountId = account_id, MaxResults = 100)
    results_dashboard = response_dashboard['DashboardSummaryList']

    while "NextToken" in response_dashboard.keys():
        response_dashboard = qs_client.list_dashboards(
            AwsAccountId = account_id, 
            MaxResults = 100, 
            NextToken = response_dashboard["NextToken"]
        )
        results_dashboard.extend(response_dashboard["DashboardSummaryList"])

    return dict(zip([x.get('Name') for x in results_dashboard], [x.get('DashboardId') for x in results_dashboard]))