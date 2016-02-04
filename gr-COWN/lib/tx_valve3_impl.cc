/* -*- c++ -*- */
/* 
 * Copyright 2016 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "tx_valve3_impl.h"




using namespace std;


namespace gr {
  namespace COWN {

    tx_valve3::sptr
    tx_valve3::make()
    {
      return gnuradio::get_initial_sptr
        (new tx_valve3_impl());
    }

    /*
     * The private constructor
     */
    tx_valve3_impl::tx_valve3_impl()
      : gr::sync_block("tx_valve3",
              gr::io_signature::make(0, 0, 0),
              gr::io_signature::make(1, 1, sizeof(gr_complex)))
    {
	senoidal.clear();
	Nsamples =  2000;
	tau = PRI = Nsamples;
	sen_index = 0;
	remaining_PRI  = 0;
	for(int k=0; k <Nsamples;  k++){
		senoidal.push_back(        exp(       gr_complex(0, 2*3.141559*(k%Nsamples)*3.0/Nsamples))                   );
		}	
		
	}

    /*
     * Our virtual destructor.
     */
    tx_valve3_impl::~tx_valve3_impl()
    {
    }

    int
    tx_valve3_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        gr_complex *out = (gr_complex *) output_items[0];
		
		//memset(out, 0x00, noutput_items*8 ); 
		 
		int Npri;
		
		Npri = int( ceil(  (remaining_PRI + PRI)*1.0/noutput_items    ));
		
		
		
		 
        for(int i =0; i <noutput_items ; i++){
			if (sen_index < Nsamples) {
			out[i]= senoidal[sen_index];
		  }else{
			  out[i] = gr_complex(0,0);
			  }
			
			if (sen_index >= Nsamples -1 + 800 ){
					sen_index =0;
			}else{ 
				sen_index++;
			}	
		}  




        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace COWN */
} /* namespace gr */

