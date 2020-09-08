$("#slider-range").slider({
    range: true,
    orientation: "horizontal",
    min: 0,
    max: 2000000,
    values: [0, 2000000],
    step: 100,
  
    slide: function (event, ui) {
      if (ui.values[0] == ui.values[1]) {
        return false;
      }
      
      $("#min_price").val(ui.values[0]);
      $("#max_price").val(ui.values[1]);
    }
  });
  