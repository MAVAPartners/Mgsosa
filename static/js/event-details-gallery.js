(function($) {
	
	"use strict";
	
	//Hide Loading Box (Preloader)
	$(window).on('load',function(){
		var pre_loader = $('.preloader')
		pre_loader.fadeOut('slow',function(){$(this).remove();});
	});
	
	//Update header style + Scroll to Top	
	$(window).on('scroll', function() {
        if ($(window).scrollTop() > 117) {
            $('.header-main').addClass('fixed-header');
			$('.scroll-to-top').fadeIn(300);
        } else {
            $('.header-main').removeClass('fixed-header');
			$('.scroll-to-top').fadeOut(300);
        }
    });
	
	//Submenu Dropdown Toggle
	if($('.header-main li.dropdown ul').length){
		$('.header-main li.dropdown').append('<div class="dropdown-btn"><span class="fa fa-angle-down"></span></div>');
		
		//Dropdown Button
		$('.header-main li.dropdown .dropdown-btn').on('click', function() {
			$(this).prev('ul').slideToggle(500);
		});
		
		
		//Disable dropdown parent link
		$('.navigation li.dropdown > a').on('click', function(e) {
			e.preventDefault();
		});
	}

	//Accordion Box
	if ($('.accordion-block').length) {
		$('.accordion-block .accordion-btn').on('click', function() {
			if ($(this).hasClass('active') !== true) {
				$('.accordion-block .accordion-btn').removeClass('active');
			}
	
			if ($(this).next('.accordion-description').is(':visible')) {
				$(this).removeClass('active');
				$(this).next('.accordion-description').slideUp(500);
			} else {
				$(this).addClass('active');
				$('.accordion-block .accordion-description').slideUp(500);
				$(this).next('.accordion-description').slideDown(500);
			}
		});
	}

	// Scroll to a Specific Div
	if($('.scroll-to-target').length){
		$(".scroll-to-target").on('click', function() {
			var target = $(this).attr('data-target');
		   // animate
		   $('html, body').animate({
			   scrollTop: $(target).offset().top
			 }, 1000);
	
		});
	}

	//gallery-slider-area
	$('.gallery-slider-area').owlCarousel({
		loop:true,
		margin:15,
		nav:true,
		smartSpeed: 3000,
		autoplay: 4000,
		navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
		responsive:{
			0:{
				items:1
			},
			400:{
				items:2
			},
			600:{
				items:3
			},
			800:{
				items:4
			},
			1200:{
				items:5
			}
		}
	});
		
	// partner-slider
	$('.partner-slider').owlCarousel({
		loop:true,
		margin:20,
		nav:true,
		smartSpeed: 3000,
		autoplay: 4000,
		navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
		responsive:{
			0:{
				items:1
			},
			400:{
				items:1
			},
			600:{
				items:2
			},
			800:{
				items:3
			},
			1200:{
				items:5
			}
		}
	});

	//Four Column Carousel Slider
	$('.four-column-carousel').owlCarousel({
		loop:true,
		margin:30,
		nav:true,
		smartSpeed: 2000,
		autoplay: 4000,
		navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
		responsive:{
			0:{
				items:1
			},
			600:{
				items:2
			},
			800:{
				items:3
			},
			1070:{
				items:4
			}
		}
	});
	
	//Two Column Carousel Slider
	$('.two-column-carousel').owlCarousel({
		loop:true,
		margin:30,
		nav:true,
		smartSpeed: 3000,
		autoplay: 4000,
		navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
		responsive:{
			0:{
				items:1
			},
			480:{
				items:1
			},
			600:{
				items:1
			},
			800:{
				items:2
			},
			1024:{
				items:2
			}
		}
	});

	//Three Column Carousel Slider
	$('.three-column-carousel').owlCarousel({
		loop:true,
		margin:30,
		nav:true,
		smartSpeed: 3000,
		autoplay: 4000,
		navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
		responsive:{
			0:{
				items:1
			},
			480:{
				items:1
			},
			600:{
				items:2
			},
			800:{
				items:2
			},
			1024:{
				items:3
			}
		}
	});
		
	//testimonial-slider-area
	$('.testimonial-slider-area').owlCarousel({
		loop:true,
		margin:30,
		nav:true,
		smartSpeed: 3000,
		autoplay: 4000,
		navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
		responsive:{
			0:{
				items:1
			},
			480:{
				items:1
			},
			600:{
				items:2
			},
			800:{
				items:2
			},
			1024:{
				items:3
			}
		}
	});
	
	
	//team-slider-area
	$('.team-slider-area').owlCarousel({
		loop:true,
		margin:30,
		nav:true,
		dots:false,
		smartSpeed: 3000,
		autoplay: 4000,
		navText: [ '<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>' ],
		responsive:{
			0:{
				items:1
			},
			480:{
				items:1
			},
			600:{
				items:2
			},
			800:{
				items:2
			},
			1024:{
				items:4
			}
		}
	});	

	// Search Toggle Btn
	    if($('.toggle-search').length){
	        $('.toggle-search').on('click', function() {
	            $('.header-search-area').slideToggle(300);
	        });
	    }

	//Custom Seclect Box
	if($('.custom-select-box').length){
		$('.custom-select-box').selectmenu().selectmenu('menuWidget').addClass('overflow');
	}	
	
	//LightBox / Fancybox
	if($('.lightbox-image').length) {
		$('.lightbox-image').fancybox({
			openEffect  : 'elastic',
			closeEffect : 'elastic',
			helpers : {
				media : {}
			}
		});
	}
	
	//=== Contact Form Validation ===
	if($("#contact-form").length){
		$("#contact-form").validate({
			submitHandler: function(form) {
			  var form_btn = $(form).find('button[type="submit"]');
			  var form_result_div = '#form-result';
			  $(form_result_div).remove();
			  form_btn.before('<div id="form-result" class="alert alert-success" role="alert" style="display: none;"></div>');
			  var form_btn_old_msg = form_btn.html();
			  form_btn.html(form_btn.prop('disabled', true).data("loading-text"));
			  $(form).ajaxSubmit({
				dataType:  'json',
				success: function(data) {
				  if( data.status == 'true' ) {
					$(form).find('.form-control').val('');
				  }
				  form_btn.prop('disabled', false).html(form_btn_old_msg);
				  $(form_result_div).html(data.message).fadeIn('slow');
				  setTimeout(function(){ $(form_result_div).fadeOut('slow') }, 6000);
				}
			  });
			}
		});
	}

	// Fact Counter	
	$(window).on('scroll', function() {
		if($('.fun-fact-counter').length){
			$('.fun-fact-counter .column.animated').each(function() {
		
				var $t = $(this),
					n = $t.find(".count-text").attr("data-stop"),
					r = parseInt($t.find(".count-text").attr("data-speed"), 10);
					
				if (!$t.hasClass("counted")) {
					$t.addClass("counted");
					$({
						countNum: $t.find(".count-text").text()
					}).animate({
						countNum: n
					}, {
						duration: r,
						easing: "linear",
						step: function() {
							$t.find(".count-text").text(Math.floor(this.countNum));
						},
						complete: function() {
							$t.find(".count-text").text(this.countNum);
						}
					});
				}
			});
		}
	});
	
	// Scroll to a Specific Div
	if($('.scroll-to-target').length){
		$(".scroll-to-target").on('click', function() {
			var target = $(this).attr('data-target');
		   // animate
		   $('html, body').animate({
			   scrollTop: $(target).offset().top
			 }, 10);
	
		});
	}

	// Elements Animation
	if($('.wow').length){
		var wow = new WOW(
		  {
			boxClass:     'wow',      // animated element css class (default is wow)
			animateClass: 'animated', // animation css class (default is animated)
			offset:       0,          // distance to the element when triggering the animation (default is 0)
			mobile:       false,       // trigger animations on mobile devices (default is true)
			live:         true       // act on asynchronously loaded content (default is true)
		  }
		);
		wow.init();
	}

})(window.jQuery);