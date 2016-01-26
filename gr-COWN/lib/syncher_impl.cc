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
#include "syncher_impl.h"

using namespace std;


namespace gr {
  namespace COWN {

    syncher::sptr
    syncher::make()
    {
      return gnuradio::get_initial_sptr
        (new syncher_impl());
    }

    /*
     * The private constructor
     */
    syncher_impl::syncher_impl()
      : gr::sync_block("syncher",
              gr::io_signature::make(1, 1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)))
    {
        set_output_multiple(4);
        set_history(200);
        counter = 0;
    }

    /*
     * Our virtual destructor.
     */
    syncher_impl::~syncher_impl()
    {
    }

    int
    syncher_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const float *in = (const float*) input_items[0];
        float *out = (float*) output_items[0];

        // Do <+signal processing+>

        // Tell runtime system how many output items we produced.

      int i = 0;
      while (in[i]!= 0xFFFFFFFF){
          i++;
      }


        for (i=0; i<noutput_items  ; i++ ){
            out[i]=in[i];
        }
        if( counter %80 ==0){
        cout << "noutput_items= " << dec <<  noutput_items  << " coutner= "<< counter << endl;

        } 
        counter ++;

        return noutput_items;
    }

  } /* namespace COWN */
} /* namespace gr */

