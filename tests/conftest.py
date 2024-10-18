import pytest
from bs4 import BeautifulSoup
from bs4.element import Tag

@pytest.fixture
def sample_row() -> Tag:
    """Fixture to provide a sample row for testing."""
    row_html = """
<tr>
			<td>
                              1
                               
                              
                            
                              
                              
                          </td><td>
                              3.5
                          </td><td>
                              <a id="ContentPlaceHolder1_GridView1_HyperLink1_0" href="/110399/player" target="_blank">Victor Wembanyama</a><span class="icon-in-doubt" data-bs-toggle="tooltip" data-bs-placement="top" title="Player is in doubt"><i class="fa fa-question-circle" aria-hidden="true"></i></span> 
                   
                              
                          </td><td>C</td><td>SA</td><td>70</td><td>31.1</td><td>
                            <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFfgpzz" id="ContentPlaceHolder1_GridView1_HFfgpzz_0">
                            <span id="ContentPlaceHolder1_GridView1_LFGP_0" class="float-start">0.473</span>
                            <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFFGP" id="ContentPlaceHolder1_GridView1_HFFGP_0" value="-0.0435170000">
                            <span class="float-end small" style="font-size: 0.7em;">(8.8/18.6)</span>
                            <br><span id="ContentPlaceHolder1_GridView1_hi12_0" class="badge" style="color: #555; width: 100%; background-color: #fff; font-weight: 400;">-0.04</span>
                        </td><td>
                              <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFftpzz" id="ContentPlaceHolder1_GridView1_HFftpzz_0">
                            <span id="ContentPlaceHolder1_GridView1_LFTP_0" class="float-start">0.802</span>
                            <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFFTP" id="ContentPlaceHolder1_GridView1_HFFTP_0" value="0.4818695000">
                            <span class="float-end small" style="font-size: 0.7em;">(4.5/5.6)</span>
<br><span id="ContentPlaceHolder1_GridView1_hi11_0" class="badge" style="color: #555; width: 100%; background-color: #fff; font-weight: 400;">0.48</span>
                        </td><td>
                                <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFtgmzz" id="ContentPlaceHolder1_GridView1_HFtgmzz_0">
                            <span id="ContentPlaceHolder1_GridView1_LTGM_0">2.0</span>
                            <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFTGM" id="ContentPlaceHolder1_GridView1_HFTGM_0" value="0.3907740944">
<br><span id="ContentPlaceHolder1_GridView1_hi2_0" class="badge" style="color: #555; width: 100%; background-color: #fff; font-weight: 400;">0.39</span>
                        </td><td class="vgood">
                                <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFptszz" id="ContentPlaceHolder1_GridView1_HFptszz_0" value="vgood">
                            <span id="ContentPlaceHolder1_GridView1_LPTS_0">24.1</span>
                            <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFPTS" id="ContentPlaceHolder1_GridView1_HFPTS_0" value="1.6173768658">
<br><span id="ContentPlaceHolder1_GridView1_hi3_0" class="badge" style="color: #555; width: 100%; background-color: #fff; font-weight: 400;">1.62</span>
                        </td><td class="elite">
                                  <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFrebzz" id="ContentPlaceHolder1_GridView1_HFrebzz_0" value="elite">
                            <span id="ContentPlaceHolder1_GridView1_LREB_0">11.6</span>
                            <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFREB" id="ContentPlaceHolder1_GridView1_HFREB_0" value="2.7094286300">
<br><span id="ContentPlaceHolder1_GridView1_hi6_0" class="badge" style="color: #555; width: 100%; background-color: #fff; font-weight: 400;">2.71</span>
                        </td><td class="good">
                                <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFastzz" id="ContentPlaceHolder1_GridView1_HFastzz_0" value="good">
                            <span id="ContentPlaceHolder1_GridView1_LAST_0">4.4</span>
                            <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFAST" id="ContentPlaceHolder1_GridView1_HFAST_0" value="0.7550735907">
<br><span id="ContentPlaceHolder1_GridView1_hi7_0" class="badge" style="color: #555; width: 100%; background-color: #fff; font-weight: 400;">0.76</span>
                        </td><td class="good">
                                 <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFstlzz" id="ContentPlaceHolder1_GridView1_HFstlzz_0" value="good">
                            <span id="ContentPlaceHolder1_GridView1_LSTL_0">1.4</span>
                            <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFSTL" id="ContentPlaceHolder1_GridView1_HFSTL_0" value="1.2079628207">
<br><span id="ContentPlaceHolder1_GridView1_hi8_0" class="badge" style="color: #555; width: 100%; background-color: #fff; font-weight: 400;">1.21</span>
                        </td><td class="elite">
                                <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFblkzz" id="ContentPlaceHolder1_GridView1_HFblkzz_0" value="elite">
                            <span id="ContentPlaceHolder1_GridView1_LBLK_0">3.9</span>
                            <input type="hidden" name="ctl00$ContentPlaceHolder1$GridView1$ctl02$HFBLK" id="ContentPlaceHolder1_GridView1_HFBLK_0" value="7.3685031363">
<br><span id="ContentPlaceHolder1_GridView1_hi9_0" class="badge" style="color: #555; width: 100%; background-color: #fff; font-weight: 400;">7.37</span>
                        </td><td>
                          <span id="ContentPlaceHolder1_GridView1_Label1_0">14.49</span>
                      </td>
		</tr>
    """
    soup = BeautifulSoup(row_html, "html.parser")
    return soup.find("tr")
