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
  namespace avio505 {

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
      : gr::block("Synchronizer",
              gr::io_signature::make(1, 1, sizeof(int)),
              gr::io_signature::make(1, 1, sizeof(int)))
    {
		set_history(200);
		set_output_multiple(7);
		flag_start = 0x00000001;
		counter = 0;
		
	}

    /*
     * Our virtual destructor.
     */
    syncher_impl::~syncher_impl()
    {
    }

    void
    syncher_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
         ninput_items_required[0] = noutput_items  + 36;
    }

    int
    syncher_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
        const int *in = (const int *) input_items[0];
        int *out = (int*) output_items[0];
		
		
		unsigned int n = 0;
		while ( (in[n]&flag_start) == 0  ){
		n++;	
		}
		
		for (int i= 0; i< noutput_items ; i++){
			out[i] = in[i+n];
			}
		
		if (n !=0){
			cout << "ERROR n different to 0 =" << n << endl;
		}
		
		counter++;
		
		if (counter %2000 ==0 ){
			
			cout<< "n =" << n <<   "  \t in[0] "<< in[0]   <<   "  \t in[1] "<< in[1] << endl;
			cout<<    "  \t\t in[2] "<< in[2]   <<   "  \t in[3] "<< in[3] << endl;
			cout<<    "  \t\t in[4] "<< in[2]   <<   "  \t in[5] "<< in[3] << endl;
			cout<< "in[n] ="<< hex << in[n] << endl;
			cout<< "in[n]&flag_start) ="<< hex << (in[n]&flag_start) << endl;
			cout<< endl;
					cout <<  "nitems_written ="<< dec << nitems_written(0) << 
				   "  nitems_read ="<< nitems_read(0) <<
				   " difference ="<< nitems_written(0)*1.0/nitems_read(0)  <<  endl;
			cout<< endl;
		}
		
        // Do <+signal processing+>
        // Tell runtime system how many input items we consumed on
        // each input stream.
        consume_each (noutput_items+n);

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace avio505 */
} /* namespace gr */

