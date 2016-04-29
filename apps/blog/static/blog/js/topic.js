$('.btn-add-post').on('click', function(e){
	e.preventDefault();
	var msg = $('#formx').serialize();
	send_post_url = $('#formx').attr('action');
	$.ajax({
		type: 'POST',
		url: send_post_url,
		data: msg,
		success: function(response) {
			if (response.status == 'ok') {
				$( ".post_load" ).load("/posts/" + "1");
			}
		},
		error:  function(xhr, str){
				alert('Возникла ошибка: ' + xhr.responseCode);
		}
	});
});




$('.edit-post-button').on('click', function(e){
	e.preventDefault();
	edit_post_url = $(this).attr('href');
	edit_post_data = $('#' + $(this).data('id'));
	$.get(edit_post_url)
	.done(function(response) {
		edit_post_data.html(response);
	})
});

$('.delete-post-button').on('click', function(e){
	e.preventDefault();
	delete_post_url = $(this).attr('href');
	delete_post_data = $('#' + $(this).data('id'));
	vote_count = $('.post_count');
	$.get(delete_post_url)
	.done(function(response) {
		delete_post_data.remove();
		var old_count = parseInt(vote_count.text(), 10);
		var new_count = old_count - 1;
		vote_count.text(new_count);
	})
});



$('.good_vote').on('click', function(e){
	e.preventDefault();

	$this = $(this);
	url = $this.attr('href');
	vote_count = $('.topic-good_vote__count');

	$.get(url)
	.done(function(response) {
		if (response.status == 'ok') {
			var old_count = parseInt(vote_count.text(), 10);
			var new_count = old_count + 1;
			vote_count.text(new_count);
		} else {
			$("#error-text").html('Вы уже проголосовали');
		}
	})
})


$('.bad_vote').on('click', function(e){
	e.preventDefault();

	$this = $(this);
	url = $this.attr('href');
	vote_count = $('.topic-bad_vote__count');

	$.get(url)
	.done(function(response) {
		if (response.status == 'ok') {
			var old_count = parseInt(vote_count.text(), 10);
			var new_count = old_count + 1;
			vote_count.text(new_count);
		} else {
			$("#error-text").html('Вы уже проголосовали');
		}
	})
})
