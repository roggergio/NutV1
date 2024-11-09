function updateTotalenergia() {
  const v_eneValue = parseFloat(document.getElementById("v_ene").value);
  const f_eneValue = parseFloat(document.getElementById("f_ene").value);
  const csg_eneValue = parseFloat(document.getElementById("csc_ene").value);
  const ccg_eneValue = parseFloat(document.getElementById("ccg_ene").value);
  const leg_eneValue = parseFloat(document.getElementById("leg_ene").value);
  const aoamb_eneValue = parseFloat(document.getElementById("aoamb_ene").value);
  const aoab_eneValue = parseFloat(document.getElementById("aoab_ene").value);
  const aoam_eneValue = parseFloat(document.getElementById("aoam_ene").value);
  const aoaa_eneValue = parseFloat(document.getElementById("aoaa_ene").value);
  const lechedes_eneValue = parseFloat(document.getElementById("lechedes").value);
  const lechesem_eneValue = parseFloat(document.getElementById("lechesem").value);
  const lecheent_eneValue = parseFloat(document.getElementById("lecheent").value);
  const lechecaz_eneValue = parseFloat(document.getElementById("lechecaz").value);
  const aceitesp_eneValue = parseFloat(document.getElementById("aceitesp_ene").value);
  const aceitecp_eneValue = parseFloat(document.getElementById("aceitecp_ene").value);
  const azucarsg_eneValue = parseFloat(document.getElementById("azucarsg_ene").value);
  const azucarcg_eneValue = parseFloat(document.getElementById("azucarcg_ene").value);




  const variables = [
    v_eneValue, f_eneValue, csg_eneValue, ccg_eneValue, leg_eneValue,
    aoamb_eneValue, aoab_eneValue, aoam_eneValue, aoaa_eneValue,
    lechedes_eneValue, lechesem_eneValue, lecheent_eneValue,
    lechecaz_eneValue, aceitesp_eneValue, aceitecp_eneValue,
    azucarsg_eneValue, azucarcg_eneValue
  ];
  
  let allValid = true;
  
  for (const variable of variables) {
    if (isNaN(variable)) {
      allValid = false;
      break;
    }
  }
  
  if (allValid) {
    const TotalenergiaValue = v_eneValue + f_eneValue + csg_eneValue + ccg_eneValue +
      leg_eneValue + aoamb_eneValue + aoab_eneValue + aoam_eneValue + aoaa_eneValue +
      lechedes_eneValue + lechesem_eneValue + lecheent_eneValue + lechecaz_eneValue +
      aceitesp_eneValue + aceitecp_eneValue + azucarsg_eneValue + azucarcg_eneValue;
  
    document.getElementById("totalene").textContent = TotalenergiaValue;
    updateTotalenergia();
  } else {
    document.getElementById("totalene").textContent = "0";
  }
  

/*                                                                            verduras */

  function verduras(input) {
    const inputValue = parseFloat(input.value);
    if (!isNaN(inputValue) ) {
      const v_eneValue = inputValue * 25;
      const v_hdcValue = inputValue * 4;
      const v_proValue = inputValue * 2;
      const v_lipValue = 0;

      document.getElementById("v_ene").textContent = v_eneValue;
      document.getElementById("v_hdc").textContent = v_hdcValue;
      document.getElementById("v_pro").textContent = v_proValue;
      document.getElementById("v_lip").textContent = v_lipValue;
      updateTotalenergia()

    } else {
      document.getElementById("v_ene").textContent = "0";
      document.getElementById("v_hdc").textContent = "0";
      document.getElementById("v_pro").textContent = "0";
      document.getElementById("v_lip").textContent = "0";
    }
    updateTotalenergia() 
  }

/*                                                                            frutas */

function frutas(input) {
  const inputValue = parseFloat(input.value);
  if (!isNaN(inputValue) ) {
    const f_eneValue = inputValue * 60;
    const f_hdcValue = inputValue * 15;
    const f_proValue = 0;
    const f_lipValue = 0;

    document.getElementById("f_ene").textContent = f_eneValue;
    document.getElementById("f_hdc").textContent = f_hdcValue;
    document.getElementById("f_pro").textContent = f_proValue;
    document.getElementById("f_lip").textContent = f_lipValue;

  } else {
    document.getElementById("v_ene").textContent = "0";
    document.getElementById("v_hdc").textContent = "0";
    document.getElementById("v_pro").textContent = "0";
    document.getElementById("v_lip").textContent = "0";
  }
  
}
/*                                                                            Cereales sin grasa */

function cereales_sg(input) {
  const inputValue = parseFloat(input.value);
  if (!isNaN(inputValue) ) {
    const csg_eneValue = inputValue * 70;
    const csg_hdcValue = inputValue * 15;
    const csg_proValue = inputValue * 2;
    const csg_lipValue = 0;

    document.getElementById("csg_ene").textContent = csg_eneValue;
    document.getElementById("csg_hdc").textContent = csg_hdcValue;
    document.getElementById("csg_pro").textContent = csg_proValue;
    document.getElementById("csg_lip").textContent = csg_lipValue;
    updateTotalenergia()
  } else {
    document.getElementById("csg_ene").textContent = "0";
    document.getElementById("csg_hdc").textContent = "0";
    document.getElementById("csg_pro").textContent = "0";
    document.getElementById("csg_lip").textContent = "0";
  }
  updateTotalenergia()
}


/*                                                                  Cereales con grasa */

function cereales_cg(input) {
  const inputValue = parseFloat(input.value);
  if (!isNaN(inputValue) ) {
    const ccg_eneValue = inputValue * 115;
    const ccg_hdcValue = inputValue * 15;
    const ccg_proValue = inputValue * 2;
    const ccg_lipValue = inputValue * 5;

    document.getElementById("ccg_ene").textContent = ccg_eneValue;
    document.getElementById("ccg_hdc").textContent = ccg_hdcValue;
    document.getElementById("ccg_pro").textContent = ccg_proValue;
    document.getElementById("ccg_lip").textContent = ccg_lipValue;
    updateTotalenergia()
  } else {
    document.getElementById("ccg_ene").textContent = "0";
    document.getElementById("ccg_hdc").textContent = "0";
    document.getElementById("ccg_pro").textContent = "0";
    document.getElementById("ccg_lip").textContent = "0";
  }
  updateTotalenergia()
}

/*                                                                         leguminosas */

function leguminosas(input) {
  const inputValue = parseFloat(input.value);
  if (!isNaN(inputValue) ) {
    const leg_eneValue = inputValue * 120;
    const leg_hdcValue = inputValue * 20;
    const leg_proValue = inputValue * 8;
    const leg_lipValue = inputValue;

    document.getElementById("leg_ene").textContent = leg_eneValue;
    document.getElementById("leg_hdc").textContent = leg_hdcValue;
    document.getElementById("leg_pro").textContent = leg_proValue;
    document.getElementById("leg_lip").textContent = leg_lipValue;
    updateTotalenergia()
  } else {
    document.getElementById("leg_ene").textContent = "0";
    document.getElementById("leg_hdc").textContent = "0";
    document.getElementById("leg_pro").textContent = "0";
    document.getElementById("leg_lip").textContent = "0";
  }
  updateTotalenergia()
}

/*                                                               origen animal muy bajo*/
function aoa_mb(input) {
  const inputValue = parseFloat(input.value);
  if (!isNaN(inputValue) ) {
    const aoamb_eneValue = inputValue * 40;
    const aoamb_hdcValue = 0;
    const aoamb_proValue = inputValue * 7;
    const aoamb_lipValue = inputValue;

    document.getElementById("aoamb_ene").textContent = aoamb_eneValue;
    document.getElementById("aoamb_hdc").textContent = aoamb_hdcValue;
    document.getElementById("aoamb_pro").textContent = aoamb_proValue;
    document.getElementById("aoamb_lip").textContent = aoamb_lipValue;
    updateTotalenergia()
  } else {
    document.getElementById("aoamb_ene").textContent = "0";
    document.getElementById("aoamb_hdc").textContent = "0";
    document.getElementById("aoamb_pro").textContent = "0";
    document.getElementById("aoamb_lip").textContent = "0";
  }
  updateTotalenergia()
}

/*                                                               origen animal bajo*/
function aoa_b(input) {
  const inputValue = parseFloat(input.value);
  if (!isNaN(inputValue) ) {
    const aoab_eneValue = inputValue * 55;
    const aoab_hdcValue = 0;
    const aoab_proValue = inputValue * 7;
    const aoab_lipValue = inputValue * 3;

    document.getElementById("aoab_ene").textContent = aoab_eneValue;
    document.getElementById("aoab_hdc").textContent = aoab_hdcValue;
    document.getElementById("aoab_pro").textContent = aoab_proValue;
    document.getElementById("aoab_lip").textContent = aoab_lipValue;
    updateTotalenergia()
  } else {
    document.getElementById("aoab_ene").textContent = "0";
    document.getElementById("aoab_hdc").textContent = "0";
    document.getElementById("aoab_pro").textContent = "0";
    document.getElementById("aoab_lip").textContent = "0";
  }
  updateTotalenergia()
}


/*                                                               origen animal moderado*/
function aoa_m(input) {
  const inputValue = parseFloat(input.value);
  if (!isNaN(inputValue) ) {
    const aoam_eneValue = inputValue * 75;
    const aoam_hdcValue = 0;
    const aoam_proValue = inputValue * 7;
    const aoam_lipValue = inputValue * 5;

    document.getElementById("aoam_ene").textContent = aoam_eneValue;
    document.getElementById("aoam_hdc").textContent = aoam_hdcValue;
    document.getElementById("aoam_pro").textContent = aoam_proValue;
    document.getElementById("aoam_lip").textContent = aoam_lipValue;
    updateTotalenergia()
  } else {
    document.getElementById("aoam_ene").textContent = "0";
    document.getElementById("aoam_hdc").textContent = "0";
    document.getElementById("aoam_pro").textContent = "0";
    document.getElementById("aoam_lip").textContent = "0";
  }
  updateTotalenergia()
}

/*                                                               origen animal altas*/
function aoa_a(input) {
  const inputValue = parseFloat(input.value);
  if (!isNaN(inputValue) ) {
    const aoaa_eneValue = inputValue * 100;
    const aoaa_hdcValue = 0;
    const aoaa_proValue = inputValue * 7;
    const aoaa_lipValue = inputValue * 8;

    document.getElementById("aoaa_ene").textContent = aoaa_eneValue;
    document.getElementById("aoaa_hdc").textContent = aoaa_hdcValue;
    document.getElementById("aoaa_pro").textContent = aoaa_proValue;
    document.getElementById("aoaa_lip").textContent = aoaa_lipValue;
    updateTotalenergia()
  } else {
    document.getElementById("aoaa_ene").textContent = "0";
    document.getElementById("aoaa_hdc").textContent = "0";
    document.getElementById("aoaa_pro").textContent = "0";
    document.getElementById("aoaa_lip").textContent = "0";
  }
  updateTotalenergia()
}




/*                                                                     leche descremada*/
function lechedes(input) {
  const inputValue = parseFloat(input.value);
  if (!isNaN(inputValue) ) {
    const lechedes_eneValue = inputValue * 95;
    const lechedes_hdcValue = inputValue * 12;
    const lechedes_proValue = inputValue * 9;
    const lechedes_lipValue = inputValue * 2;

    document.getElementById("lechedes_ene").textContent = lechedes_eneValue;
    document.getElementById("lechedes_hdc").textContent = lechedes_hdcValue;
    document.getElementById("lechedes_pro").textContent = lechedes_proValue;
    document.getElementById("lechedes_lip").textContent = lechedes_lipValue;
    updateTotalenergia()
  } else {
    document.getElementById("lechedes_ene").textContent = "0";
    document.getElementById("lechedes_hdc").textContent = "0";
    document.getElementById("lechedes_pro").textContent = "0";
    document.getElementById("lechedes_lip").textContent = "0";
  }
  updateTotalenergia()
}

/*                                                                 leche semidescremada*/
function lechesem(input) {
  const inputValue = parseFloat(input.value);
  if (!isNaN(inputValue) ) {
    const lechesem_eneValue = inputValue * 110;
    const lechesem_hdcValue = inputValue * 12;
    const lechesem_proValue = inputValue * 9;
    const lechesem_lipValue = inputValue * 4;

    document.getElementById("lechesem_ene").textContent = lechesem_eneValue;
    document.getElementById("lechesem_hdc").textContent = lechesem_hdcValue;
    document.getElementById("lechesem_pro").textContent = lechesem_proValue;
    document.getElementById("lechesem_lip").textContent = lechesem_lipValue;
    updateTotalenergia()
  } else {
    document.getElementById("lechesem_ene").textContent = "0";
    document.getElementById("lechesem_hdc").textContent = "0";
    document.getElementById("lechesem_pro").textContent = "0";
    document.getElementById("lechesem_lip").textContent = "0";
  }
  updateTotalenergia()
}

/*                                                                        leche entera*/
function lecheent(input) {
  const inputValue = parseFloat(input.value);
  if (!isNaN(inputValue) ) {
    const lecheent_eneValue = inputValue * 150;
    const lecheent_hdcValue = inputValue * 12;
    const lecheent_proValue = inputValue * 9;
    const lecheent_lipValue = inputValue * 8;

    document.getElementById("lecheent_ene").textContent = lecheent_eneValue;
    document.getElementById("lecheent_hdc").textContent = lecheent_hdcValue;
    document.getElementById("lecheent_pro").textContent = lecheent_proValue;
    document.getElementById("lecheent_lip").textContent = lecheent_lipValue;
    updateTotalenergia()
  } else {
    document.getElementById("lecheent_ene").textContent = "0";
    document.getElementById("lecheent_hdc").textContent = "0";
    document.getElementById("lecheent_pro").textContent = "0";
    document.getElementById("lecheent_lip").textContent = "0";
  }
  updateTotalenergia()
}

/*                                                                     leche con azucar*/
function lechecaz(input) {
  const inputValue = parseFloat(input.value);
  if (!isNaN(inputValue) ) {
    const lechecaz_eneValue = inputValue * 200;
    const lechecaz_hdcValue = inputValue * 12;
    const lechecaz_proValue = inputValue * 8;
    const lechecaz_lipValue = inputValue * 5;

    document.getElementById("lechecaz_ene").textContent = lechecaz_eneValue;
    document.getElementById("lechecaz_hdc").textContent = lechecaz_hdcValue;
    document.getElementById("lechecaz_pro").textContent = lechecaz_proValue;
    document.getElementById("lechecaz_lip").textContent = lechecaz_lipValue;
    updateTotalenergia()
  } else {
    document.getElementById("lechecaz_ene").textContent = "0";
    document.getElementById("lechecaz_hdc").textContent = "0";
    document.getElementById("lechecaz_pro").textContent = "0";
    document.getElementById("lechecaz_lip").textContent = "0";
  }
  updateTotalenergia()
}




/*                                                        aceites y grasas sin proteina*/
function aceitessp(input) {
  const inputValue = parseFloat(input.value);
  if (!isNaN(inputValue) ) {
    const aceitesp_eneValue = inputValue * 45;
    const aceitesp_hdcValue = 0;
    const aceitesp_proValue = 0;
    const aceitesp_lipValue = inputValue * 5;

    document.getElementById("aceitesp_ene").textContent = aceitesp_eneValue;
    document.getElementById("aceitesp_hdc").textContent = aceitesp_hdcValue;
    document.getElementById("aceitesp_pro").textContent = aceitesp_proValue;
    document.getElementById("aceitesp_lip").textContent = aceitesp_lipValue;
    updateTotalenergia()
  } else {
    document.getElementById("aceitesp_ene").textContent = "0";
    document.getElementById("aceitesp_hdc").textContent = "0";
    document.getElementById("aceitesp_pro").textContent = "0";
    document.getElementById("aceitesp_lip").textContent = "0";
  }
  updateTotalenergia()
}
/*                                                        aceites y grasas con proteina*/
function aceitescp(input) {
  const inputValue = parseFloat(input.value);
  if (!isNaN(inputValue) ) {
    const aceitecp_eneValue = inputValue * 70;
    const aceitecp_hdcValue = inputValue * 3;
    const aceitecp_proValue = inputValue * 3;
    const aceitecp_lipValue = inputValue * 5;

    document.getElementById("aceitecp_ene").textContent = aceitecp_eneValue;
    document.getElementById("aceitecp_hdc").textContent = aceitecp_hdcValue;
    document.getElementById("aceitecp_pro").textContent = aceitecp_proValue;
    document.getElementById("aceitecp_lip").textContent = aceitecp_lipValue;
    updateTotalenergia()
  } else {
    document.getElementById("aceitecp_ene").textContent = "0";
    document.getElementById("aceitecp_hdc").textContent = "0";
    document.getElementById("aceitecp_pro").textContent = "0";
    document.getElementById("aceitecp_lip").textContent = "0";
  }
  updateTotalenergia()
}






/*                                                                   azucares sin grasa*/
function azucarsg(input) {
  const inputValue = parseFloat(input.value);
  if (!isNaN(inputValue) ) {
    const azucarsg_eneValue = inputValue * 40;
    const azucarsg_hdcValue = inputValue * 10;
    const azucarsg_proValue = 0;
    const azucarsg_lipValue = 0;

    document.getElementById("azucarsg_ene").textContent = azucarsg_eneValue;
    document.getElementById("azucarsg_hdc").textContent = azucarsg_hdcValue;
    document.getElementById("azucarsg_pro").textContent = azucarsg_proValue;
    document.getElementById("azucarsg_lip").textContent = azucarsg_lipValue;

  } else {
    document.getElementById("azucarsg_ene").textContent = "0";
    document.getElementById("azucarsg_hdc").textContent = "0";
    document.getElementById("azucarsg_pro").textContent = "0";
    document.getElementById("azucarsg_lip").textContent = "0";
  }
  
}
/*                                                                   azucares con grasa*/
function azucarcg(input) {
  const inputValue = parseFloat(input.value);
  if (!isNaN(inputValue) ) {
    const azucarcg_eneValue = inputValue * 85;
    const azucarcg_hdcValue = inputValue * 10;
    const azucarcg_proValue = 0;
    const azucarcg_lipValue = inputValue * 5;

    document.getElementById("azucarcg_ene").textContent = azucarcg_eneValue;
    document.getElementById("azucarcg_hdc").textContent = azucarcg_hdcValue;
    document.getElementById("azucarcg_pro").textContent = azucarcg_proValue;
    document.getElementById("azucarcg_lip").textContent = azucarcg_lipValue;

  } else {
    document.getElementById("azucarcg_ene").textContent = "0";
    document.getElementById("azucarcg_hdc").textContent = "0";
    document.getElementById("azucarcg_pro").textContent = "0";
    document.getElementById("azucarcg_lip").textContent = "0";
  }
  
}