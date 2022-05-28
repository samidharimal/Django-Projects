

$(document).ready(function(){
    $(".full").on("click", function(){
        var rating = $(this).data("rating")
        var fantacy_id = $(this).parent().data("fantacy_id")
        $.ajax({
            url: '/fantasy-rate/',
            method: 'post',
            data: {
                rating: rating,
                fantacy_id: fantacy_id,
                csrfmiddlewaretoken: csrf_token
            },
            success: function(resp){
                if (resp.success == "true"){
                    alert(`Successfully rated ${resp.rating}`)
                }else{
                    alert('Something went wrong, please try again.')
                }
                location.reload()
            }
        })
    })
})