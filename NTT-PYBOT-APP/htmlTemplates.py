css = '''
<style>
.chat-message {
    padding: 0.8rem;
    border-radius: 15px;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
.chat-message.user {
    background-color: #5C6BC0;  /* Dark blue */
    color: #ffffff;
    justify-content: flex-end;
    margin-left: auto;
}
.chat-message.bot {
    background-color: #FFFFFF;  /* White */
    color: #333333;
    justify-content: flex-start;
    margin-right: auto;
}
.chat-message .avatar {
    width: 60px;
    height: 60px;
    flex-shrink: 0;
    display: flex;
    justify-content: center;
    align-items: center;
}
.chat-message .avatar img {
    width: 100%;
    height: auto;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    font-size: 16px;
    padding: 10px 20px;
    max-width: calc(100% - 80px);  /* Leaving space for avatar */
    word-wrap: break-word;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/Wz446GM/pybottt.png" alt="pybottt" border="0">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/HrXtBjC/nttdata.jpg" alt="user avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
