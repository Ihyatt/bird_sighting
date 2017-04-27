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
function sightingSubmitted() {
	// check for succes of AJAX request
}
function submitSighting() {
	console.log("here")
	var submitBird = $("#bird_species").val();
	var submitQuantity = $("#quantity").val();
	var submission = {
		"bird": submitBird,
		"quantity": submitQuantity
	};
	if (submitBird.trim()) {
		console.log("here")
		$.post("/submit-bird", submission, sightingSubmitted);
		$("#bird_species").val("")
		$("#quantity").val("")
}
}
$("#add-sighting").click(submitSighting)




// JS for wanting to see all birds and probability 

function showAllBirds(results){
	var returnedAllBirds = results;
		$("#all-birds").append("<div style='margin-top:10px;margin-bottom:10px;'>" + "Here are the chances you have to see le birds!" + "</div>")

	for (var key in returnedAllBirds){
	$("#all-birds").append("<li>" + key + " " + returnedAllBirds[key] + "%" +  "</li>")
 };


}

function viewAllBirds() {
	$.get("/return-all-birds.json", showAllBirds);
	$("#view-probabilities").html("refresh le probabilities");
	$("#all-birds").html("")
}


$("#view-probabilities").click(viewAllBirds)