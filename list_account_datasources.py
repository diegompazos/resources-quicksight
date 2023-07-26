def list_account_datasources(qs_client, account_id, aws_region):
    response_data_source = qs_client.list_data_sources(
        AwsAccountId = account_id,
        MaxResults = 100
    )
    results_data_source = response_data_source['DataSources']

    while "NextToken" in response_data_source:
        response_data_source = qs_client.list_data_sources(
            AwsAccountId = account_id,
            MaxResults = 100,
            NextToken=response_data_source["NextToken"]
        )
        results_data_source.extend(response_data_source["DataSources"])

    return dict(zip([x.get('Name') for x in results_data_source], [x.get('DataSourceId') for x in results_data_source]))