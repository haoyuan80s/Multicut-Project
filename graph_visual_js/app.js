var width = 4000,
    height = 2000

var color = d3.scaleOrdinal(d3.schemeCategory20);

var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height);

// visual layout
var simulation = d3.forceSimulation()
    .force("center", d3.forceCenter(width / 2, height / 2))
    .force("charge", d3.forceManyBody())
    .force("link", d3.forceLink().id(function(d) {return d.id; })
           .distance(function(d) {
	       return 500;
	       //return 1/(d.value/scale)
	   })
);

d3.json("facebook.json", function(error, json) {
    if (error) throw error;

    var refreshGraph = function() {
	
	scale = 10*Math.max.apply(null, json.links.map(function(x) {return x.value}));
	
	simulation
	    .nodes(json.nodes);
  
	simulation
	    .force("link")
	    .links(json.links);

	var edges = svg.selectAll(".link").data(json.links)
	var link = edges
	    .enter().append("line")
	    .attr("class", "link")
	    .merge(edges)
	    .attr("stroke-width", function(d) {
	    	return Math.sqrt(d.value); });
	
	var nodes = svg.selectAll(".node").data(json.nodes)
	var node = nodes
	    .enter().append("g")
	    .attr("class", "node")
	    .merge(nodes)

	node.append("circle")
	    .attr("r", 10)
	    .attr("fill", function(d) { return color(d.group); })
	    .attr("id", function(d) {return d.id; })
            .call(d3.drag()
	    	  .on("start", dragstarted)
	    	  .on("drag", dragged)
	    	  .on("end", dragended))
  
  	node.append("text")
	    .attr("dx", 12)
	    .attr("dy", ".35em")
	    .text(function(d) { return d.id });

	simulation.on("tick", function() {
	    link.attr("x1", function(d) { return d.source.x; })
		.attr("y1", function(d) { return d.source.y; })
		.attr("x2", function(d) { return d.target.x; })
		.attr("y2", function(d) { return d.target.y; });
	
	    node.attr("transform",
		      function(d) { return "translate(" + d.x + "," + d.y + ")"; });
	});
    }

    refreshGraph();
    
    
    // musical notes
    // let piano = Synth.createInstrument('piano');
    let instrument = Synth.createInstrument('piano');    
    let num2note = "ABCDEFG"
    let prevNote = null
    let currNote = null

    d3.select("body")
	.on("keydown", function() {
            // svg.append("text")
            //     .attr("x","5")
            //     .attr("y","150")
            //     .style("font-size","50px")
            //     .text("keyCode: " + d3.event.keyCode)  
            //   .transition().duration(2000)
            //     .style("font-size","5px")
            //     .style("fill-opacity",".1")
            //     .remove();
	    
	    // enlarge selected note
	    let note_name = num2note[d3.event.keyCode % 7];
	    instrument.play(note_name,4,2);
	    d3.select("#"+note_name)
		.attr("transform", "scale(1.2)")
		.transition().duration(200)
		.attr("transform", "");
	    prevNote = currNote
	    currNote = note_name
	    // add link from previous node to current node
	    let links = simulation.force("link").links()
	    let nodes = simulation.nodes()
	    
	    let link_ = links.filter(function(l) {
		return (l.source.id === prevNote && l.target.id === currNote+"'");
	    })[0];

	    if (link_) {
 	    	link_.value += 1
	    } else if (prevNote) {
		let s = nodes.filter(function(n) {return n.id == prevNote})[0];
		let t = nodes.filter(function(n) {return n.id == currNote+"'"})[0];
		if (s != t) {
	    	    link_ = {source: s, target: t, value: 1};
	    	    json.links.push(link_);
		    refreshGraph();
		}
	    }
	    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
	    
	});
    
    
});

  // for drag event
function dragstarted(d) {
  if (!d3.event.active) simulation.alphaTarget(0.3).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(d) {
  d.fx = d3.event.x;
  d.fy = d3.event.y;
}

function dragended(d) {
  if (!d3.event.active) simulation.alphaTarget(0);
  d.fx = null;
  d.fy = null;
}


