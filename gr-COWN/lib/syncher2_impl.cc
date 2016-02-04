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
#include "syncher2_impl.h"

using namespace std;

namespace gr {
  namespace COWN {

    syncher2::sptr
    syncher2::make()
    {
      return gnuradio::get_initial_sptr
        (new syncher2_impl());
    }

    /*
     * The private constructor
     */
    syncher2_impl::syncher2_impl()
      : gr::block("syncher2",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)))
    {
      counter = 0;
      set_output_multiple(4);

    }

    /*
     * Our virtual destructor.
     */
    syncher2_impl::~syncher2_impl()
    {
    }

    void
    syncher2_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
        
        ninput_items_required[0] = noutput_items + 16;
    }

    int
    syncher2_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
        const float  *in = (const float*) input_items[0];
        float *out = (float*) output_items[0];
        
        const int  *in_int = (const int*) input_items[0];
 
        

          int n = 0;
          while (in_int[n] != 0xFFFFFFFF){
            cout << "LOST SAMPLES n delayed = " << n <<endl;
            n++;
          }


        int i = 0;
        for (i=0; i<noutput_items  ; i++ ){
            out[i]=in[i+n];

                  //unsigned long int timestamp;
                  //timestamp = nitems_written(0) + i;

                   //if (timestamp % 512 == 0 ){


                            //uint64_t aesc =  timestamp ;

                            //float counterfloat = 1.000*out[i];


                            //// const pmt::pmt_t key = pmt::string_to_symbol("count");
                            //// const pmt::pmt_t value = pmt::from_float   (  counterfloat );
                            //// const pmt::pmt_t srcid = pmt::string_to_symbol("cnt");
                            //// add_item_tag(0,   aesc , key, value, srcid);

                   //}

        }


        if( counter %2000 ==0){
        //cout << "\t\tnoutput_items= " << dec <<  noutput_items  << "\tninput_items= "  <<  ninput_items[0]<<  " n="<<n  << endl;

        //cout << "in_int[0] = "<< hex <<in_int[0]   << "\tin_int[1] = "<< hex <<in_int[1]  << "\tin_int[2] = " << in_int[2]   << "\tin_int[3] = " << in_int[3]  << endl;
        
        // cout << "in[0] = "<< dec<<in[0]   << "\tin[1] = " <<in[1]  << "\tin[2] = " << in[2]   << "\tin[3] = " << in[3]          << endl;

        	 
					//cout <<  "nitems_written ="<< dec << nitems_written(0) << 
				   //"  nitems_read ="<< nitems_read(0) << " Time= " <<  nitems_read(0)/2e6  <<
				   //" Ratio ="<< nitems_written(0)*1.0/nitems_read(0)  <<  endl;
			       //cout<< endl;
        
        
        
        } 
        counter ++;

        consume_each (noutput_items+n);
 
        return noutput_items;
    }

  } /* namespace COWN */
} /* namespace gr */

