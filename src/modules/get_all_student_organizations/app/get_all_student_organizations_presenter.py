from .get_all_student_organizations_controller import GetAllStudentOrganizationsController
from .get_all_student_organizations_usecase import GetAllStudentOrganizationsUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo = Environments.get_user_repo()()
usecase = GetAllStudentOrganizationsUsecase(repo)
controller = GetAllStudentOrganizationsController(usecase)

def lambda_handler(event, context):
    
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
    response = httpResponse.toDict()
    
    return response