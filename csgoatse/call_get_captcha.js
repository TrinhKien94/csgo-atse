function calculate_color_to_bet(){
    var image_data ={'image' : 'test.phm','count':'1'};
    $.ajax({
		url: "http://127.0.0.1:5002/messages",
		dataType: 'json',
		type: 'POST',
		headers: {
			'Accept': 'application/json',
			'Content-Type': 'text/plain'
		},
		data: JSON.stringify(image_data),
		processData: false,
		success: function( data, textStatus, jQxhr ){
			console.log('ok');
		},
		error: function( jqXhr, textStatus, errorThrown ){
			console.log( errorThrown );
		}
	});
}