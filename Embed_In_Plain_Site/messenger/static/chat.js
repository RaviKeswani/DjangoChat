$('#chat-form').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url : 'post/',
        type : 'POST',
        data : { msgbox : $('#chat-msg').val() },

        success : function(json){
            console.log(json);
            $('#chat-msg').val('');
            $('#msg-list').append('<li class="text-right list-group-item">' + json.msg + '</li>');
            var chatlist = document.getElementById('msg-list-div');
            chatlist.scrollTop = chatlist.scrollHeight;
        }
    });
});



function getMessages(){

        $.get('messages/', function(messages){
            console.log(messages);
            $('#msg-list').html(messages);
            var chatlist = document.getElementById('msg-list-div');
            chatlist.scrollTop = chatlist.scrollHeight;
        });


}

$(function(){

    refreshTimer = setInterval(getMessages, 100);
});


/* For disabling send button in home.html if content is null*/
$(document).ready(function() {
     $('#send').attr('disabled','disabled');
     $('#chat-msg').keyup(function() {
        if($(this).val() != '') {
            $('#send').removeAttr('disabled');
        }
        else {
            $('#send').attr('disabled','disabled');
        }
     });
 });

