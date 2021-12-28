
//задаем цвет кнопки выбора исходя из выбора в каталоге
boldText = document.querySelectorAll("button.my_button");
boldText.forEach((item, i) => {
item.onclick = function () {
let css_img;
let url_img;
let id_img;

  document.querySelector('#m_odnotonra').hidden = false;
  css_img = ($(boldText[i]).css("background-image"));
  document.querySelector('#m_odnotonra').style.backgroundImage = css_img;
  console.log(css_img);
//вписываю ссылку на картинку для установки на кнопке выбора
  url_img = $(boldText[i]).attr("src");
  document.querySelector('#m_odnotonra').setAttribute('src', url_img);
//вписываю id выбранной ткани для передачи
  id_img = $(boldText[i]).attr("id");
  document.querySelector('#m_odnotonra').setAttribute('alt', id_img);

  console.log(id_img);


}
});


//удаляем с кнопки установленный стиль выбора
cancelText = document.querySelectorAll("#m_odnoton_del");
cancelText.forEach((item, i) => {
  item.onclick = function () {
  document.querySelector('#m_odnotonra').style.backgroundImage = "url()";
  document.querySelector('#m_odnotonra').setAttribute('src', " ");
  document.querySelector('#m_odnotonra').hidden = true;

    }

});

//загружаем индивидуалку
cancelText = document.querySelectorAll("#m_odnoton_ind");
cancelText.forEach((item, i) => {
  item.onclick = function () {
  document.querySelector('#m_odnotonra').style.backgroundImage = "url()";
  document.querySelector('#m_odnotonra').setAttribute('src', " ");
  document.querySelector('#m_odnotonra').hidden = true;

    }

});


function fun1()	{
var rng=document.getElementById("r1");
var p=document.getElementById("one");
p.innerHTML=rng.value;
};


function fun2()	{
var rng=document.getElementById("r2");
var p=document.getElementById("one2");
};


function fun1()	{
var rng=document.getElementById("r3");
var p=document.getElementById("one3");
};

//подвешиваем на кнопку скрытие/показ значка окружение
$(document).ready(function(){
    $("#environment_m").click(function(){
        $("#environment_on").show();
        $("#environment_m").hide();

    });
    $("#environment_on").click(function(){
        $("#environment_m").show();
        $("#environment_on").hide();
    });
});

//подвешиваем на кнопку скрытие/показ значка избранное
$(document).ready(function(){
  $("#head_off").click(function(){
      $("#head_on").show();
      $("#head_off").hide();
  });


  $("#head_on").click(function(){
        $("#head_off").show();
        $("#head_on").hide();

    });

});

//подвешиваем на кнопку скрытие/показ значка изображения профиль/анфа
$(document).ready(function(){
  $("#view_1").click(function(){
      $("#view_2").show();
      $("#view_1").hide();
  });


  $("#view_2").click(function(){
        $("#view_1").show();
        $("#view_2").hide();

    });

});

//подвешиваем на кнопку скрытие/показ значка изображения вопрос-аннотации
$(document).ready(function(){
  $("#question_on").click(function(){
      $("#question_off").show();
      $("#question_on").hide();
  });


  $("#question_off").click(function(){
        $("#question_on").show();
        $("#question_off").hide();

    });

});

// get pdf
var sale_pdf = document.getElementById("sale_pdf");

// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("main_sale");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

sale_pdf.onclick = function generatePDF() {
  const element = document.getElementById("modal-content2");

  html2pdf()
  .from(element)
  .save("zakaz");
}
