function toggleDocs(event)
{
	if (event.target && event.target.className == 'block-name')
	{
		var next = event.target.nextElementSibling;
		
		if (next.style.visibility == "hidden")
		{
			next.style.visibility = "visible";
			next.style.height = "100px";
			next.style.opacity = "1";
			next.style.animation = "transitionin 0.9s";
		} 
		else
		{
			next.style.visibility = "hidden";
			next.style.height = "1px";
			next.style.animation = "transitionback 0.6s";
		}
	}
}
document.addEventListener('click', toggleDocs, true);