/**
*	Site-specific configuration settings for Highslide JS
*/
hs.graphicsDir = 'static/js/highslide/graphics/';
hs.showCredits = false;
hs.outlineType = 'custom';
hs.align = 'center';
hs.dimmingOpacity = 0.75;
hs.headingOverlay.position = 'leftpanel';


// Add the slideshow controller
hs.addSlideshow({
	slideshowGroup: 'group1',
	interval: 5000,
	repeat: false,
	useControls: true,
	fixedControls: 'fit',
	overlayOptions: {
		className: 'large-dark',
		opacity: 0.6,
		position: 'bottom center',
		offsetX: 0,
		offsetY: -15,
		hideOnMouseOut: true
	}
});

// gallery config object
var config1 = {
	slideshowGroup: 'group1',
	transitions: ['expand', 'crossfade']
};
