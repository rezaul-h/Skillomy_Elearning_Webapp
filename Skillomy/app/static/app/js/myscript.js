$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 4,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 4,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})
$('.remove-cart').click(function(){
    var id =$(this).attr("pid").toString();
    var eml=this;
    //console.log(id);

    $.ajax({
        type:'GET',
        url:"/removecart",
        data:{prod_id: id},
        success: function(data){
            //console.log("delete");
            document.getElementById("total_ammount").innerText=data.total_ammount;
            document.getElementById("total_discount").innerText=data.total_discount;
            document.getElementById("total_actual").innerText=data.total_actual;
            eml.ParentNode.ParentNode.ParentNode.ParentNode.remove();
        }
    }

    )

    })
