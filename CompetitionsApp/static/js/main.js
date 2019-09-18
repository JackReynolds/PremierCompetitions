// Glide
try{
  const glide = new Glide('.glide', {
    type: 'carousel',
    startAt: 0,
    focusAt: 'center',
    autoplay: 3000,
    perView: 3,
    breakpoints: {
      800: {perview: 2},
      400: {perView: 1}
    }
  })
  glide.mount();
}
catch(err){
  // pass
}


// How It Works Section Text Appear 
function scrollAppear(){
  try {
    const howItWorksText = document.querySelector('.how-it-works-text');
    const introPosition = howItWorksText.getBoundingClientRect().top;
    const screenPosition = window.innerHeight/1.5;
    const howItWorksTitle = document.querySelector('.how-it-works-heading')
    const screenPosition2 = window.innerHeight/1.2;

    if(introPosition < screenPosition2){
      howItWorksTitle.classList.add('how-it-works-text-appear');
    }

    if(introPosition < screenPosition){
      howItWorksText.classList.add('how-it-works-text-appear');
    }
  }
  catch {
    // pass
  }
}

window.addEventListener('scroll', scrollAppear);

// Using jQuery to fade out the errors / warnings after 3 seconds
setTimeout(function(){
  $('#message').fadeOut('slow');
}, 3000);


navBar = document.querySelector('.navbar'); 
if (window.innerWidth < 700) {
  navBar.classList.add('fixed-top');
}

// function testAppear(){
//   const test = document.querySelector('.test');
//   const introPosition = test.getBoundingClientRect().top;
//   const screenPosition = window.innerHeight/2;

//   if(introPosition < screenPosition){
//     test.classList.add('test-appear');
//   }
// }

// window.addEventListener('scroll', testAppear);

 // Need to understand how to set timer for clock
//  function getTimeRemaining(endtime) {
//    var t = Date.parse(endtime) - Date.parse(new Date());
//    var seconds = Math.floor((t / 1000) % 60);
//    var minutes = Math.floor((t / 1000 / 60) % 60);
//    var hours = Math.floor((t / (1000 * 60 * 60)) % 24);
//    var days = Math.floor(t / (1000 * 60 * 60 * 24));
//    return {
//      'total': t,
//      'days': days,
//      'hours': hours,
//      'minutes': minutes,
//      'seconds': seconds
//    };
//  }
 
//  function initializeClock(id, endtime) {
//    var clock = document.getElementById(id);
//    var daysSpan = clock.querySelector('.days');
//    var hoursSpan = clock.querySelector('.hours');
//    var minutesSpan = clock.querySelector('.minutes');
//    var secondsSpan = clock.querySelector('.seconds');
 
//    function updateClock() {
//      var t = getTimeRemaining(endtime);
 
//      daysSpan.innerHTML = t.days;
//      hoursSpan.innerHTML = ('0' + t.hours).slice(-2);
//      minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
//      secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);
 
//      if (t.total <= 0) {
//        clearInterval(timeinterval);
//      }
//    }
 
//    updateClock();
//    var timeinterval = setInterval(updateClock, 1000);
//  }
 
//  var deadline = new Date(Date.parse(new Date()) + 15 * 24 * 60 * 60 * 1000);
//  initializeClock('clockdiv', deadline);

 // Countdown attempt 2 
 const countdown = document.querySelector('.countdown-timer');

 // Launch date - need to change the below to the end date of the competition
 // const endDate = new Date('Jan 1, 2020 13:00:00').getTime();


 // const endDate = new Date(`${endDateTime} 13:00:00`).getTime();

 endDateTime = document.querySelector('.end-date');

 const endDate = new Date(`${endDateTime.innerHTML} 12:00:00`).getTime();


  // Update every second 
  const interval = setInterval(() => {
  const now = new Date().getTime();
  // Distance from now and end date 
  const distance = endDate - now;

  // Time calculations
  const days = Math.floor(distance/(1000 * 60 * 60 * 24));
  const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display result 
  countdown.innerHTML = `
    <div>${days}<span class="countdown-text"> Days</span></div>
    <div>${hours}<span class="countdown-text"> Hours</span></div>
    <div>${minutes}<span class="countdown-text"> Minutes</span></div>
    <div>${seconds}<span class="countdown-text"> Seconds</span></div>
  `;

  // If launch date is passed 
  if(distance < 0){
    // Stop countdown
    clearInterval(interval);
    // Style and output some text 
    countdown.style.color = "#17a2b8";
    countdown.innerHTML = 'Draw taking place soon, check details on page!'
  }
}, 1000);
