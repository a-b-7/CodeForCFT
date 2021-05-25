import troposphere.events as events
from troposphere import Ref, Template
from troposphere import Base64, GetAtt,FindInMap
import troposphere.awslambda as awslambda
from troposphere.s3 import Bucket
import troposphere.serverless as Serverless
''' 


rProductEventRule


'''
t = Template()


eventRule = events.Rule(title = "", template=None,validation=True,Description = " AWS Event Rule for S3 Product object folder",)
eventBus =  events.EventBus(title="",template=None,validation=True,eventBus = ,)
