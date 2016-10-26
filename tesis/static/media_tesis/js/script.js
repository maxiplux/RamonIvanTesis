$(document).ready(function(){
	$('#icon_indice a').click(function(){
			
		if(	$('.content_menu').css('display')=="none"){	
			$('#icon_indice').addClass('closer_black');					
			$('#icon_extras, #icon_autores').addClass('unselected');				
			$('#iconed_menu').addClass('blured');				
			$('#content').addClass('blured');			
		}else{
			$('#icon_indice').removeClass('closer_black');	
			$('#icon_extras, #icon_autores').removeClass('unselected');
			$('#iconed_menu').removeClass('blured');
			$('#content').removeClass('blured');	
		}
		$('.content_menu').fadeToggle();
		
	});
	$('a.pri_fil').click(function(){
		$('.dorpdowned').slideUp();
		$(this).parent().find('.dorpdown').slideToggle();
	})
	$('.dorpdown a.sec_fil').click(function(){
		$(this).parent().find('.dorpdowned').slideToggle();
	})
	$('a.e').click(function(e){
		e.preventDefault();
	})
	$( "#iconed_menu" ).on( "click",  function() {
		if($(this).hasClass('ini')){
			$('#icon_menu').fadeIn(700);
			$(this).removeClass('ini fin').addClass('fin');
			$('#icon_indice').fadeIn().delay(100).animate({
				'margin-top':'0'			
			},200);
			$('#icon_extras').fadeIn().delay(150).animate({
				'margin-top':'0'			
			},200);
			$('#icon_autores').fadeIn().delay(200).animate({
				'margin-top':'0'			
			},200);		
		}else{
			$('#icon_menu').fadeOut(150)
			$(this).removeClass('fin').addClass('ini');			
			$('#icon_menu li').animate({
				'margin-top':'-80px'			
			},200);	
			//if(	$('.content_menu').css('display')=="block"){					
				$('.content_menu').fadeOut();				
			//}				
			$('.dorpdown, .dorpdowned').slideUp();
			$(' #icon_indice, #icon_extras, #icon_autores').removeClass('unselected closer_black');
			$('#iconed_menu').removeClass('blured');			
			$('#content').removeClass('blured');		
				
		}
	});
})