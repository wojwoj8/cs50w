document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  // send email button
  document.querySelector('#compose-form').addEventListener('submit', send_email)
  //document.querySelector('#archive').onclick(load_mailbox('archive'));
  //document.querySelector('#archive').addEventListener('click', () => load_mailbox('archive'));

  // By default, load the inbox
  load_mailbox('inbox');


});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#read-email').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#read-email').style.display = 'none';
  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  // load mail

  //sent mail
  if (mailbox === 'sent'){

  fetch('/emails/sent')

  .then(response => response.json())
  .then(emails => {
      // Print emails
      //console.log(emails);
      emails.forEach(email => {
        const div = document.createElement('div')
        div.setAttribute("class", "inboxcont");
        //div.innerHTML = '<b>' + email.sender + '</b>' + email.subject + '   ' + email.timestamp;
        div.innerHTML = `<p class="sender"><b>To: ${email.recipients}</b> ${email.subject}</p>  <p class="date"> ${email.timestamp} </p> `;
        
        document.querySelector('#emails-view').append(div);
        //read_email(email.id)
        div.addEventListener('click', function(){
            read_email(email.id, mailbox);
        } )

      });; 
});
}
  if(mailbox === 'inbox'){
    //console.log(mailbox)
    fetch('/emails/inbox')

  .then(response => response.json())
  .then(emails => {
      // Print emails
      //console.log(emails);
        emails.forEach(email => {
        const div = document.createElement('div')
        div.setAttribute("class", "inboxcont");
        //div.innerHTML = '<b>' + email.sender + '</b>' + email.subject + '   ' + email.timestamp;
        div.innerHTML = `<p class="sender"><b>From: ${email.sender}</b> ${email.subject}</p>  <p class="date"> ${email.timestamp} </p> `;
        if (email.read === true){
          div.style.backgroundColor = "#dddddd";
        }
        document.querySelector('#emails-view').append(div);
        //read_email(email.id)
        div.addEventListener('click', function(){
            read_email(email.id, mailbox);
        } )
      });;
});
  }
  if(mailbox === 'archive'){
    //console.log(mailbox)
    fetch('/emails/archive')

  .then(response => response.json())
  .then(emails => {
      
      //console.log(emails);
        emails.forEach(email => {
        const div = document.createElement('div')
        div.setAttribute("class", "inboxcont");
        //div.innerHTML = '<b>' + email.sender + '</b>' + email.subject + '   ' + email.timestamp;
        div.innerHTML = `<p class="sender"><b>${email.sender}</b> ${email.subject}</p>  <p class="date"> ${email.timestamp} </p> `;
        if (email.read === true){
          div.style.backgroundColor = "#bbbbbb";
        }
        document.querySelector('#emails-view').append(div);
        //read_email(email.id)
        div.addEventListener('click', function(){
            read_email(email.id, mailbox);
        } )
      });;
});
  }
}

function send_email(){
  event.preventDefault();
  const recipients = document.querySelector('#compose-recipients').value;
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value;
  //console.log('test');
  fetch('/emails',{
    method:'POST',
    body: JSON.stringify({
      recipients:`${recipients}`,
      subject:`${subject}`,
      body:`${body}`
    })
  })
  .then(() => load_mailbox('sent'));
  return false;
  
}

function read_email(email, mailbox){

  const sent = mailbox;
  //console.log(sent)
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#read-email').style.display = 'block';
  //const id = document.querySelector('#emails-view').querySelector('div').id;
  //console.log(email);
  fetch(`/emails/${email}`)
  .then(response => response.json())
  .then(data => {
    //console.log(data)
    const div = document.querySelector('#read-email');
    let btn = document.createElement("button");
    let btn1 = document.createElement("button");
    if (data.archived == false){
      btn.innerHTML = "Archive";
      var x = true;
    }
    else{
      btn.innerHTML = "Unarchive";
      var x = false;
    }
    
    btn.setAttribute('class', 'btn btn-sm btn-outline-primary');
    btn.setAttribute('id', 'archive');

    btn1.setAttribute('class', 'btn btn-sm btn-outline-primary');
    btn1.setAttribute('id', 'reply');
    btn1.innerHTML = "Reply";
    
    
    //div.setAttribute("class", 'read');
    //console.log(data.body)
    div.innerHTML = `
    <div class="readdata"> 
      <div class="from">
        <b>From: </b>${data.sender}
        <br>
      </div>
      <b>To: </b>${data.recipients}<br>
      <b>Subject: </b> ${data.subject}<br> 
      <b>Timestamp: </b>${data.timestamp} <br><hr> 
      <p>${data.body}</p>\
    </div>` ;
    //archive
    document.querySelector('.from').append(btn1)
    
    //console.log(sent)
    // if sent hide archive
    if (sent != 'sent'){
      //console.log('dziala')
      document.querySelector('.from').append(btn)
    }

    btn.addEventListener('click', function(){
      fetch(`/emails/${email}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: x
        })   
    })
    .then(() => load_mailbox('archive'))
    })
    btn1.addEventListener('click', function(){
      compose_email();
      document.querySelector('#compose-recipients').disabled = true;
      document.querySelector('#compose-recipients').value = `${data.sender}`;
      if (data.subject.slice(0,4) === "Re: "){
      document.querySelector('#compose-subject').value = `${data.subject}`;
      }
      else{
      document.querySelector('#compose-subject').value = `Re: ${data.subject}`;
      }
      document.querySelector('#compose-body').value = `\nOn ${data.timestamp} ${data.sender} wrote: \n${data.body}\n`;

    })

    if (data.read === false){
    fetch(`/emails/${email}`, {
      method: 'PUT',
      body: JSON.stringify({
          read: true
      })
  })
}
});

}
