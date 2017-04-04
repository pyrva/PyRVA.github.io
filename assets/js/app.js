/*! apollo.js v1.7.0 | (c) 2014 @toddmotto | https://github.com/toddmotto/apollo */
(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define(factory);
  } else if (typeof exports === 'object') {
    module.exports = factory;
  } else {
    root.apollo = factory();
  }
})(this, function () {

  'use strict';

  var apollo = {};

  var hasClass, addClass, removeClass, toggleClass;

  var forEach = function (items, fn) {
    if (Object.prototype.toString.call(items) !== '[object Array]') {
      items = items.split(' ');
    }
    for (var i = 0; i < items.length; i++) {
      fn(items[i], i);
    }
  };

  if ('classList' in document.documentElement) {
    hasClass = function (elem, className) {
      return elem.classList.contains(className);
    };
    addClass = function (elem, className) {
      elem.classList.add(className);
    };
    removeClass = function (elem, className) {
      elem.classList.remove(className);
    };
    toggleClass = function (elem, className) {
      elem.classList.toggle(className);
    };
  } else {
    hasClass = function (elem, className) {
      return new RegExp('(^|\\s)' + className + '(\\s|$)').test(elem.className);
    };
    addClass = function (elem, className) {
      if (!hasClass(elem, className)) {
        elem.className += (elem.className ? ' ' : '') + className;
      }
    };
    removeClass = function (elem, className) {
      if (hasClass(elem, className)) {
        elem.className = elem.className.replace(new RegExp('(^|\\s)*' + className + '(\\s|$)*', 'g'), '');
      }
    };
    toggleClass = function (elem, className) {
      (hasClass(elem, className) ? removeClass : addClass)(elem, className);
    };
  }

  apollo.hasClass = function (elem, className) {
    return hasClass(elem, className);
  };

  apollo.addClass = function (elem, classes) {
    forEach(classes, function (className) {
      addClass(elem, className);
    });
  };

  apollo.removeClass = function (elem, classes) {
    forEach(classes, function (className) {
      removeClass(elem, className);
    });
  };

  apollo.toggleClass = function (elem, classes) {
    forEach(classes, function (className) {
      toggleClass(elem, className);
    });
  };

  return apollo;

});

// stuff for all pages

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
