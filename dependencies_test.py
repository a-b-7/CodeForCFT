import troposphere.events as events
from troposphere import Ref, Template
from troposphere import Base64, FindInMap,GetAtt
import troposphere.awslambda as awsLambda

t = Template()


eventRule = events.Rule(title="rAppflowRunEnd",template=None,validation=True,Description = "Event CFT Module", EventPattern = {"source": ["aws.appflow"],"detail-type": ["AppFlow End Flow Run Report"]})
target = events.Target(title = "target",Arn = "rABCLambdaAppflowIntegration",Id ="AppflowLogsFunction")
abc = t.add_output([eventRule,target])
# t.add_resource(target)
# alpha = GetAtt(abc ,"rAppflowRunEnd")
# t.add_output([alpha])
# print(t.to_json())
#...........................................................
#   rPermissionForRuleToInvokeLambda: lambda def for ABCLambdaAppflowIntegration



appflow_integration_permission  =  awsLambda.Permission(title ="rPermissionForRuleToInvokeLambda",template =None,validation=True,Action ="lambda:InvokeFunction",Principal ="events.amazonaws.com",SourceArn ="AppflowRunEnd",FunctionName = "rABCLambdaAppflowIntegration")
t.add_output([appflow_integration_permission])
print(t.to_json())  # implementation in json file
print(t.to_yaml()) # implementation in yaml
