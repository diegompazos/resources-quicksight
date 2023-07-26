def list_account_analysis(qs_client, account_id, aws_region):
    response_analysis = qs_client.list_analyses(AwsAccountId = account_id, MaxResults = 100)
    results_analysis = response_analysis['AnalysisSummaryList']

    while "NextToken" in response_analysis.keys():
        response_analysis = qs_client.list_analyses(
            AwsAccountId = account_id, 
            MaxResults = 100, 
            NextToken=response_analysis["NextToken"]
        )
        results_analysis.extend(response_analysis["AnalysisSummaryList"])
        
    return dict(zip([x.get('Name') for x in results_analysis], [x.get('AnalysisId') for x in results_analysis]))