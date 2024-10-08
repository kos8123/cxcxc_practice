from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from service import UserService
from model import SessionLocal
from pydantic import BaseModel
import os
import json

router = APIRouter()

class UserCreate(BaseModel):
    name: str
    height: float
    weight: float

class Test(BaseModel):
    key: str
  

def get_db():
    db = SessionLocal()  
    try:
        yield db        #https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#sub-dependencies-with-yield
    finally:
        db.close()

# handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))
# configuration = Configuration(access_token=os.getenv("ACCESS_TOKEN"))
# genai.configure(api_key=os.getenv("API_KEY"))



@router.get("/api/test")
def HelloWorld():
    return "Hello World"

@router.post("/api/test")
def test(cxcxc: Test):
    if cxcxc.key == "cxcxc":
        return {"message": "Succeeded"}
    else:
        return {"message": "Failed"}
    

@router.get("/api/user")
def get_allUsers(db: Session = Depends(get_db)):
    service = UserService(db)
    users = service.list_allUser()
    return [{"name":user.name, "height": user.height, "weight": user.weight} for user in users]

@router.post("/api/user")
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        service.add_user(user.name, user.height, user.weight)
        return {"status": "successed"}
    except Exception as e:
        return {"status": "error"}

# @router.post("/api/llm")
# async def linebot(request: Request, db: Session = Depends(get_db)):
#     body = await request.body()
#     body = body.decode()
#     json_data = json.loads(body)

#     try:
#         signature = request.headers['X-Line-Signature']
#         handler.handle(body, signature)
#         event = json_data['events'][0]
#         reply_token = event['replyToken']
#         user_id = event['source']['userId']
#         msg_type = event['message']['type']
            
#         if msg_type == "text":
#             msg = event['message']['text']
#             with ApiClient(configuration) as api_client:
#                 line_bot_api = MessagingApi(api_client)
#                 line_bot_api.show_loading_animation(ShowLoadingAnimationRequest(
#                 chatId=user_id, loadingSeconds=20))

#                 model = genai.GenerativeModel('gemini-1.5-flash')
#                 response = model.generate_content(f"Only parse the three attributes of name(str)/weight(float)/height(float) in the sentence, and return Json format after parsing, No symbols required, just json.{msg}")
#                 reply_msg = response.text
#                 line_bot_api.reply_message(ReplyMessageRequest(reply_token=reply_token,messages=[TextMessage(text="新增使用者成功"),]))
#                 service = UserService(db)
#                 reply_msg = json.loads(reply_msg)
#                 service.add_user(reply_msg["name"], float(reply_msg["height"]), float(reply_msg["weight"]))
        
#         else:
#                 with ApiClient(configuration) as api_client:
#                     line_bot_api = MessagingApi(api_client)
#                     line_bot_api.reply_message(
#                         ReplyMessageRequest(reply_token=reply_token,messages=[TextMessage(text='你傳的不是文字訊息'),]))

#     except Exception as e:
#         detail = e.args[0]
#         print(detail)




    
