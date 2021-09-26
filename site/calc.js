function check() {
    document.getElementById("output").innerHTML = document.getElementById("name").value + ", вам положены следующие льготы и выплаты: ";
    
    // беременная
    if (document.getElementById("female").checked == true &&
        mf.health[mf.health.selectedIndex].value == "Беременность")
    {
        document.getElementById("output").innerHTML += "Ежемесячное пособие с момента постановки на учет (от 6 до 12 недель) и до рождения ребенка. Оформление родового сертификата на оплату медицинских услуг по сопровождению беременности и родам. ";
        if (mf.status[mf.status.selectedIndex].value == "Трудоустроенный") {
            document.getElementById("output").innerHTML += "Выплата декретных на момент ухода в отпуск по беременности и родам."
        }
    }
    
    // многодетная
    if (mf.kids[mf.kids.selectedIndex].value == "Есть" &&
       document.getElementById("countKids").value >= 3)
    {
        document.getElementById("output").innerHTML += "Бесплатная выдача лекарств, приобретаемых по рецептам врачей (фельдшеров), для детей до достижения ими возраста 6 лет и 6 месяцев. Компенсация стоимости проезда на внутригородском транспорте для учащихся общеобразовательных организаций, профессиональных образовательных организаций, обучающихся по программам подготовки квалифицированных рабочих (служащих), путем выдачи проездных билетов. Субсидии на строительство, реконструкцию, капитальный ремонт и приобретение жилых помещений за счет средств бюджета Удмуртской Республики при условии признания многодетной семьи, нуждающейся в улучшении жилищных условий. ";
    }
    
    // безработица
    if (mf.status[mf.status.selectedIndex].value == "Безработный" &&
        ((document.getElementById("male").checked == true &&
         document.getElementById("age").value >= 17 &&
         document.getElementById("age").value <= 64)
         ||
         (document.getElementById("female").checked == true &&
          document.getElementById("age").value >= 17 &&
          document.getElementById("age").value <= 59)))
    {
        document.getElementById("output").innerHTML += "Оформление пособия по безработице. Постановка на учет в центре занятости. Участие в программе профессиональной переподготовки. "
    }
    
    // пенсия
    if ((document.getElementById("male").checked == true && document.getElementById("age").value >= 65) ||
         (document.getElementById("female").checked == true && document.getElementById("age").value >= 60))
    {
        document.getElementById("output").innerHTML += "Оформление пенсии. Льготный или бесплатный проезд на муниципальном транспорте. "
        if (document.getElementById("age").value > 80 || 
            (mf.health[mf.health.selectedIndex].value == "Инвалидность" && 
             mf.disability[mf.disability.selectedIndex].value == 1)) {
            document.getElementById("output").innerHTML += "Надбавка к пенсии. ";
        }
    }
    
    //инвалидность
    if (mf.health[mf.health.selectedIndex].value == "Инвалидность")
    {
        if (mf.status[mf.status.selectedIndex].value == "Несовершеннолетний" ||
            mf.status[mf.status.selectedIndex].value == "Пенсионер")
        {
            document.getElementById("output").innerHTML += "Социальная пенсия. ";
        }
        if (mf.status[mf.status.selectedIndex].value == "Безработный" ||
            mf.status[mf.status.selectedIndex].value == "Трудоустроенный")
        {
            document.getElementById("output").innerHTML += "Трудовая пенсия. ";
        }
        document.getElementById("output").innerHTML += "Оформление ежемесячной денежной выплаты.";
    }
}
// document.getElementById("health").selectedIndex.value == "Беременность"
//alert(document.getElementById("name").value);