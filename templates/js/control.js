function getAbsolutePath() {
	var loc = window.location;
	var pathName = loc.pathname.substring(0, loc.pathname.lastIndexOf('/') + 1);
	return loc.href.substring(0, loc.href.length - ((loc.pathname + loc.search + loc.hash).length - pathName.length));
}
jQuery(document).ready(function($) {
	$(".right").click(function() {
		$.ajax({url: getAbsolutePath()+"move/1",}).done(function() {
			console.log("right")
		});
	});
	$(".left").click(function() {
		$.ajax({url: getAbsolutePath()+"move/0",}).done(function() {
			console.log("left")
		});
	});
});