$(window).on("scroll", function() {
	if ($(window).scrollTop())
	{
		$('nav').removeClass('web-nav-class');
		$('nav').addClass('web-nav-class-back');
	}
	else 
	{
		$('nav').removeClass('web-nav-class-back');
		$('nav').addClass('web-nav-class');
	}
})