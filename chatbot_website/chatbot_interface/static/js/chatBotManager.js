

(function(){
	var chatBotManager = (new function() {
		var self = this;
		var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
		self.connection = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat");

		for (var i in eventMixin) {
			self[i] = eventMixin[i];
		}

		self.connection.onmessage = function(message) {
			var parsedData = JSON.parse(message.data);
			self.trigger('newMessage', parsedData.message);
		};

		self.send = function(message) {
			var jsonMessage = JSON.stringify({
				message:message
			});
			self.connection.send(jsonMessage);
		};
	});

	window.chatBotManager = chatBotManager;
}()); 	




