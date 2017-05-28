// Credits goes to https://blog.heroku.com/in_deep_with_django_channels_the_future_of_real_time_apps_in_django

$(function() {
    var chat_zone = $("#chat_zone");
    var isNeedSroll = function() {
        return document.documentElement.scrollHeight != document.documentElement.offsetHeight;
    };

    var scrollToBottom = function() {
        $("html, body").animate({ scrollTop: $(document).height() }, "slow");
    };

    chatBotManager.on('newMessage', function(message) {
        chat_zone.append(
            $("<p class='answer'></p>").html('Бот: ' + message)
        );

        if(isNeedSroll()) {
            scrollToBottom();
        }
    });

    $("#chat_form").on("submit", function(event) {

        try {
            var message_elem = $('#message');
            var message_val = message_elem.val().trim();
            if (!message_val) {
                return;
            }

            chatBotManager.send(message_val);
            message_elem.val('').focus();
            chat_zone.append(
                $("<p class='question'></p>").text('Вы: ' + message_val)
            );
        }
        catch(err) {
            console.error(err.message);
        }

        return false;
    });
});
