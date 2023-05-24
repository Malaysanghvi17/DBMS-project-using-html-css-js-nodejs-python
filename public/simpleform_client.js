const form = document.getElementById('form');

function displaygenderValue() {
    var ele1 = document.getElementsByName('gender');

    for(i = 0; i < ele1.length; i++) {
        if(ele1[i].checked)
            return ele1[i].value;
    }
}

function displaycourseValue() {
    var ele2 = document.getElementsByName('course');

    for(i = 0; i < ele2.length; i++) {
        if(ele2[i].checked)
            return ele2[i].value;
    }
}

form.addEventListener('submit', (event) => {
    event.preventDefault();
    const name = document.getElementById('f1').value;
    const roll = document.getElementById('f2').value;
    const email = document.getElementById('f3').value;
    const contact = document.getElementById('f4').value;
    const address = document.getElementById('f5').value;
    const birthdate = document.getElementById('f6').value;
    const gender = displaygenderValue();
    const course = displaycourseValue();
    const courseid = document.getElementById('f16').value;
    const stream = document.getElementById('f13').value;
    const semester = document.getElementById('f14').value;
    const cgpa = document.getElementById('f15').value;
    const hobby = document.getElementById('f8').value;
    const about = document.getElementById('f9').value;
    const data = { name, roll, email, contact, address, birthdate, gender, course, courseid, stream, semester, cgpa, hobby, about};
    console.log(name, roll, email, contact, address, birthdate, gender, course, courseid, stream, semester, cgpa, hobby, about);
    fetch('/submit-form', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => {
            if (response.ok) {
                window.location.replace('/success.html');
            } else {
                throw new Error('Form submission failed.');
            }
        })
        .catch(error => console.error(error));
});



// v1 ////////////////////////////////////////////////////////////////////////////////////
// const form = document.getElementById('form');

// function displaygenderValue() {
//     var ele1 = document.getElementsByName('gender');
      
//     for(i = 0; i < ele1.length; i++) {
//         if(ele1[i].checked)
//             return ele1[i].value;
//     }
// }

// function displaycourseValue() {
//     var ele2 = document.getElementsByName('course');
      
//     for(i = 0; i < ele2.length; i++) {
//         if(ele2[i].checked)
//             return ele2[i].value;
//     }
// }

// form.addEventListener('submit', (event) => {
//     event.preventDefault();
//     const name = document.getElementById('f1').value;
//     const roll = document.getElementById('f2').value;
//     const email = document.getElementById('f3').value;
//     const contact = document.getElementById('f4').value;
//     const address = document.getElementById('f5').value;
//     const birthdate = document.getElementById('f6').value;
//     const gender = displaygenderValue();
//     const course = displaycourseValue();
//     const courseid = document.getElementById('f16').value;
//     const stream = document.getElementById('f13').value;
//     const semester = document.getElementById('f14').value;
//     const cgpa = document.getElementById('f15').value;
//     const hobby = document.getElementById('f8').value;
//     const about = document.getElementById('f9').value;
//     const data = { name, roll, email, contact, address, birthdate, gender, course, courseid, stream, semester, cgpa, hobby, about};
//     console.log(name, roll, email, contact, address, birthdate, gender, course, courseid, stream, semester, cgpa, hobby, about);
//     fetch('/submit-form', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(data),
//     })
//         .then(response => response.text())
//         .then(data => console.log(data))
//         .catch(error => console.error(error));
// });

