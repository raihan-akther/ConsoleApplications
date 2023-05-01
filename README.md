# ConsoleApplications
## step 1

    ```py
        console.log("test string");
    ```

## step 2==== //Ajax JQuery for GET method

        $(document).ready(function () {
            $("#load-page").click(function () {
                $.ajax({
                    url: "/Home/Single",
                    type: "GET",
                    dataType: "html",
                    success: function (result) {
                        $("#page-content").html(result);
                    },
                    error: function () {
                        alert("An error occurred while loading the page.");
                    }
                });
            });
        });

        //Ajax JQuery for POST method

        $(document).ready(function () {
            $("#my-form").submit(function (event) {
                event.preventDefault();
                var formData = $(this).serialize();
                $.ajax({
                    url: "/Home/Single",
                    type: "POST",
                    data: formData,
                    dataType: "json",
                    success: function (result) {
                        $("#result").html("CustomerName: " + result.name + "<br>Gender: " + result.gender);
                    },
                    error: function () {
                        alert("An error occurred while submitting the data.");
                    }
                });
            });
        });


## step 3
