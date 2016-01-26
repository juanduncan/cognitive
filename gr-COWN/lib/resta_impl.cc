/* -*- c++ -*- */
/* 
 * Copyright 2015 <+YOU OR YOUR COMPANY+>.
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
#include "resta_impl.h"


#include <iostream>
#include <volk/volk.h>

using namespace std;

namespace gr {
  namespace COWN {

    resta::sptr
    resta::make()
    {
      return gnuradio::get_initial_sptr
        (new resta_impl());
    }

    /*
     * The private constructor
     */
    resta_impl::resta_impl()
      : gr::sync_block("resta",
              gr::io_signature::make(1, 1, sizeof(int)),
              gr::io_signature::make(1, 1, sizeof(int))
              
              ),
              count_errors(0), counter(0), diferencia(0), last_input(0)
    {
		
    set_history(6);
		
		}

    /*
     * Our virtual destructor.
     */
    resta_impl::~resta_impl()
    {
    }


	
		
    int
    resta_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
      const unsigned int *in = (const unsigned int*) input_items[0];

      int *out = (int*)output_items[0];
		  counter++;

      int ninput = 0;

      
		    
		in+=5;
		 
        int i ;
        for(i = 0; i < noutput_items; i++){
			  diferencia = in[i] -  in[i-1] ;




                  //unsigned long int timestamp;
                  //timestamp = nitems_written(0) + i;

                   //if (timestamp % 1000 == 0 ){


                            //uint64_t aesc =  timestamp ;

                            //float counterfloat = 1.000*out[i];


                            //const pmt::pmt_t key = pmt::string_to_symbol("count");
                            //const pmt::pmt_t value = pmt::from_float   (  counterfloat );
                            //const pmt::pmt_t srcid = pmt::string_to_symbol("cnt");
                            //add_item_tag(0,   aesc , key, value, srcid);

                   //}

			
            			if(diferencia!=80){
							
							if (nitems_written(0) > 20000){
								if( (i==0) and (  (in[i]-last_input) == 80)   ){
									//cout<< "! i =" << i<< "\tin[i]-last_input= " <<  in[i]-last_input <<endl;
								}else{
									count_errors++;
							

									cout << "\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" << endl;		
									cout << "The dif is not 80, it is x" << hex << diferencia << "\t equal =" << 
											dec << diferencia << "\tin[i-1=" <<i-1 <<"]= "<< in[i-1]<< 
											"\n time difference="<< diferencia/5e5 << "(secs)"<<
											"\tin[i]= " << in[i] << "\tdiff betw errors = " <<
											  mark_w - in[0]   <<
											"\tcount_errors="<< dec << count_errors << "\n" <<  endl;

										mark_w = in[0];
								}
							}		
            			
            			}
						

 
		}
		last_input = in[noutput_items - 1];
		memcpy(out, in, noutput_items*4);
		// if(  counter%250 == 1  ){
				
		// 	cout<< "nitems_written(0) \t"<< nitems_written(0)  << endl;
		// }
			
        return (noutput_items);





    }

  } /* namespace COWN */
} /* namespace gr */

