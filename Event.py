import troposphere.events as events
from troposphere import Ref, Template
from troposphere import Base64, FindInMap,GetAtt
import troposphere.awslambda as awsLambda
from troposphere.s3 import Bucket
import troposphere.serverless as Serveless # aws_serveeless_function

t = Template()
target_1 = events.Target(title = "Target",Arn = " arn _ rVeevaLoadingStrategyLambda" , Id = "LoadingAppflow")
target_2  = events.Target(title = "Target",Arn = " arn _ rVeevaLoadingStrategyLambda" , Id = "LoadingAppflow")


eventRule = events.Rule(title="rAppflowRunEnd",template=None,validation=True,Description = "Event CFT Module", EventPattern = {"source": ["aws.appflow"],"detail-type": ["AppFlow End Flow Run Report"]},Targets = [target_2, target_1])
# target_1 = events.RunCommandTarget(title = "Tareget",Key= " arn", Values = ["AppflowLogsFunction"])

# target_2 = events.Target(Title = )
# abc = t.add_output([eventRule,target])
t.add_resource([ eventRule])
# alpha = GetAtt(abc ,"rAppflowRunEnd")
# t.add_output([alpha])
# print(t.to_json())
#...........................................................

#............................................................
'''

 IMPLEMENTATION OF TWO TARGETS FROM EVENT RULE


'''
#   rPermissionForRuleToInvokeLambda: lambda def for ABCLambdaAppflowIntegration



appflow_integration_permission  =  awsLambda.Permission(title ="rPermissionForRuleToInvokeLambda",template =None,validation=True,Action ="lambda:InvokeFunction",Principal ="events.amazonaws.com",SourceArn ="arn_rAppflowRunEnd",FunctionName = "rABCLambdaAppflowIntegration")
t.add_resource([appflow_integration_permission])
# print(t.to_yaml())


# templating rVeevaLoading Strategy
# aws serverless function>............................................


code_ur_bucket = Serveless.S3Location(title = None , Bucket = " ",Key = " ",Version = "" )
aws_env = awsLambda.Environment(title = None,Variables =['SNOW_LAMBDA','MASTER_CONFIG_PATH','CONFIGURATION_ITEM','APPFLOW_NAME_PREFIX'] )

awsServerlessfunction  = Serveless.Function(title = "rVeevaLoadingStrategyLambda",template=None, validation= True,Description = "Lambda function to invoke appflow and load data",CodeUri =code_ur_bucket,FunctionName = "edb_commercial_veeva_appflow_loading_strategy_automation",Timeout = 900,Runtime =" python3.7",Handler=" loading_strategy_automation.lambda_handler",MemorySize = 2048,Environment =aws_env,Role ="arn:aws:iam::${AWS::AccountId}:role/${pLambdaServiceRole}" )
t.add_resource([awsServerlessfunction])
# print(t.to_yaml())
'''

Implementing rABCLambdaAppflowIntegration



'''


code_ur_bucket_abc = Serveless.S3Location(title = None , Bucket = " ",Key = " ",Version = "" )
aws_env_abc = awsLambda.Environment(title = None,Variables =['LOGGING_LEVEL','REGION_NAME','CONFIGURATION_ITEM'] )
awsServerlessfunctionabc  = Serveless.Function(title = "rABCLambdaAppflowIntegration",template=None, validation= True,Description = " Get Appflow logs",CodeUri =code_ur_bucket_abc,FunctionName = "edb_commercial_vvpm_abc_appflow_logs",Timeout = 900,Runtime =" python3.7",Handler="log_appflow_execution.handler",MemorySize = 2048,Environment =aws_env_abc,Role ="arn:aws:iam::${AWS::AccountId}:role/${pLambdaServiceRole}" )
t.add_resource([awsServerlessfunctionabc])
print(t.to_yaml())
