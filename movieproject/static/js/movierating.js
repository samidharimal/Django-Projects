
console.log('hi,js is working');

$(document).ready(function(){
    $(".ratingfull").on("click", function(){
        var rating = $(this).data("rating")
        var movie_id = $(this).parent().data("movie_id")
        $.ajax({
            url: '/allmovies-rate/',
            method: 'post',
            data: {
                rating: rating,
                movie_id: movie_id,
                csrfmiddlewaretoken: csrf_token
            },
            success: function(resp){
                if (resp.success == "true"){
                    alert(`Successfully rated ${resp.rating}`)
                }else{
                    alert('Ups!Something went wrong, please try again.')
                }
                location.reload()
            }
        })
    })
})