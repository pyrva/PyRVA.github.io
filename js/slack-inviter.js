var slackinviter = new Vue({
  el: '#slack-component',
  data: {
    state: 'unsubmitted',
    buttonthrobber: false,
    submitted: false,
    subscribed: false,
    subscribe_endpoint: 'https://c43faoh1ic.execute-api.us-east-1.amazonaws.com/prod/invite',
    email: '',
  },
  methods: {
    subscribe: function(event) {

      if (this.email.length == 0) return;

      this.buttonthrobber = true;

      fetch(this.subscribe_endpoint, {
        method: 'POST',
        mode: 'cors',
        body: JSON.stringify({
          'email': this.email
        })
      }).then(function(response) {
        return response.json();
      }).then(this.handle_response);

    },
    handle_response: function(response) {
      this.buttonthrobber = false;
      if (response.ok === true) {
        this.state = 'success';
      } else {
        if (response.error === 'already_invited' || response.error === 'already_in_team')
        {
          this.state = response.error;
        } else {
          this.state = 'error';
        }
      }
    }
  }
});
