/* globals apollo: false, Modernizr: false */

// establish variables
var nav = document.getElementsByClassName('main-nav__list')[0],
  navToggleButton = document.getElementsByClassName('main-nav__toggle')[0];

//nav toggle function
var navToggle = function(e){
  'use strict';

  apollo.toggleClass(nav, 'closed open');
  e.preventDefault();
  e.stopPropagation();
};

// if screen is smaller than 'desk' size
if(Modernizr.mq('only all and (max-width: 64em)')){

  // show toggle and collapse menu
  apollo.addClass(nav, 'active closed');

  // add touch/click event
  navToggleButton.addEventListener('touchstart', function(e){
    'use strict';

    navToggle(e);
  }, false);

  navToggleButton.addEventListener('click', function(e){
    'use strict';

    navToggle(e);
  }, false);

}

// if screen is desk size or larger

if(Modernizr.mq('only all and (min-width: 64em)')) {

  // check if scrolled
  var scrolled = false,
      html = document.getElementsByTagName("html")[0],
      body = document.getElementsByTagName("body")[0];

  var checkForScroll = function () {
    'use strict';

    if (body.scrollTop > 0) {
      scrolled = true;
      apollo.addClass(html, 'scrolled');
    }else{
      scrolled = false;
      apollo.removeClass(html, 'scrolled');
    }
    
    window.requestAnimationFrame(checkForScroll);
    
  };

  window.requestAnimationFrame(checkForScroll);
}
