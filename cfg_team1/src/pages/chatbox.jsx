import 'deep-chat-react';
import './Home.css';

const ChatBox = () => {
    return(
    <deep-chat class='chatBox-Size'
    connect='{
        "url": "http://ec2-3-80-140-21.compute-1.amazonaws.com:3000/query",
        "method": "POST",
        "headers": {"Content-Type": "application/json"}
      }' 
        images="true"
></deep-chat>
    )
};

export default ChatBox;