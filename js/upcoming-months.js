var monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
var dayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", ];


Vue.component('upcoming-event', {
  template: '#upcoming-template',
  props: ['event'],
  computed: {
    startTime: function(){
      var date = new Date(this.event.time);
      var out = [];
      var time = date.getHours();
      var isPM = time > 11;
      var hour = isPM ? time - 12 : time
      out.push(dayNames[date.getDay()]);
      out.push(', ');
      out.push(monthNames[date.getMonth()]);
      out.push(' ');
      out.push(date.getDate());
      out.push(' at ');
      out.push(hour);
      out.push(':' + date.getMinutes());
      out.push(isPM ? 'pm' : 'am');
      return out.join('');
    },
    rsvpCount: function(){
      var ev = this.event;
      return ev.yes_rsvp_count + ev.maybe_rsvp_count
    },
    rsvpText: function() {
      var isOne = this.rsvpCount === 1;
      var people = isOne ? ' person has' : ' people have';
      return this.rsvpCount + people
    }
  },
});

var upcomingApp = new Vue({
  data: {
    upcomingEvents: []
  },
  el: '#upcoming',
  // components: 
});
