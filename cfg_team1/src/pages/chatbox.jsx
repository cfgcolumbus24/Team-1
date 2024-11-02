import 'deep-chat-react';
import './Home.css';

const ChatBox = () => {
    return(
    <deep-chat class='chatBox-Size'
    connect='{
    "url": "https://customapi.com/message",
    "method": "POST",
    "headers": {"customName": "customHeaderValue"},
    "additionalBodyProps": {"customBodyField": "customBodyValue"}}'
></deep-chat>
    )
};

export default ChatBox;