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
#include "check_flux_impl.h"

using namespace std;
namespace gr {
  namespace avio505 {

    check_flux::sptr
    check_flux::make()
    {
      return gnuradio::get_initial_sptr
        (new check_flux_impl());
    }

    /*
     * The private constructor
     */
    check_flux_impl::check_flux_impl()
      : gr::block("check_flux",
              gr::io_signature::make(1, 1, sizeof(int)),
              gr::io_signature::make(1,1,  sizeof(int)))
    {}

    /*
     * Our virtual destructor.
     */
    check_flux_impl::~check_flux_impl()
    {
    }

    void
    check_flux_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
       ninput_items_required[0] = noutput_items;
    }

    int
    check_flux_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
        const int *in = (const int *) input_items[0];
        int *out = (int*) output_items[0];

        // Do <+signal processing+>
        // Tell runtime system how many input items we consumed on
        // each input stream.
        consume_each (ninput_items[0]);
		
		for(int i = 0;  i < noutput_items ; i++){
			out[i] = in[i];
			}

		cout <<  "nitems_written ="<< dec << nitems_written(0) << 
				   "  nitems_read ="<< nitems_read(0) <<
				   " difference ="<< nitems_written(0)*1.0/nitems_read(0) << endl <<  endl;

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace avio505 */
} /* namespace gr */

