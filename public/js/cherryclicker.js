function incrementScore() {
	score += 1;
	$('#score').text(score);
}

function loadSound(url) {
	var sound = document.createElement('audio');
	sound.setAttribute('src', url);
	return sound;
}

var score = 0;
var coinSound = loadSound('audio/coin.wav')

$('#thebutton').click(function() {
	incrementScore();
	coinSound.play();
});