// JS to show the best time for a sighting for a particular bird

function showChanceSighting(results) {
	var returnedBird = results;
	$("#bird-sighting").append("<div style='margin-top:10px;margin-bottom:10px;'>" + "Here are the time(s) you should check out Le Bird!" + "</div>")

	for (var key in returnedBird){
	$("#bird-sighting").append("<li>" + returnedBird[key] +" " + key + "</li>")
 };
	$("#search").val("")
}

function getProbability() {
	var searchBird = $("#search").val();	
	var search_bird = {
		"bird": searchBird
	};
	$.get("/return-search.json", search_bird, showChanceSighting);
	$("#bird-sighting").html("")
}

$(".search-sighting").click(getProbability)

// JS for submitting bird sightings

function submitSighting() {
	var submitBird = $("#bird_species").val();
	var submitQuantity = $("#quantity").val();
	var submitTime = $("#time-submit").val();

	var submission = {
		"bird": submitBird,
		"quantity": submitQuantity,
		"time":submitTime
	};
	if (submitBird.trim()) {
		$.post("/submit-bird", submission);
		$("#bird_species").val("")
		$("#quantity").val("")
		$("#time-submit").val("")
}
}

$("#add-sighting").click(submitSighting)

// JS for wanting to see all birds and probability for a particular time given

function showAllBirds(results){
	var returnedAllBirds = results;
		$("#all-birds").append("<div style='margin-top:10px;margin-bottom:10px;'>" + "Here are the chances you have to see le birds!" + "</div>")

	for (var key in returnedAllBirds){
	$("#all-birds").append("<li>" + key + " " + returnedAllBirds[key] + "%" +  "</li>")
 };
}

function viewAllBirds() {
	var submitTime = $("#time-probability").val();
	var submission ={
		"time": submitTime
	};
	$.get("/return-all-birds.json",submission, showAllBirds);
	$("#view-probabilities").html("refresh le probabilities");
	$("#all-birds").html("")
}

$("#view-probabilities").click(viewAllBirds)