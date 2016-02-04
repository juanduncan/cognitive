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
#include "test_impl.h"

namespace gr {
  namespace COWN {

    test::sptr
    test::make()
    {
      return gnuradio::get_initial_sptr
        (new test_impl());
    }

    /*
     * The private constructor
     */
    test_impl::test_impl()
      : gr::sync_block("test",
              gr::io_signature::make(1,1, sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(float)))
    {}

    /*
     * Our virtual destructor.
     */
    test_impl::~test_impl()
    {
    }

    int
    test_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const int *in = (const int*) input_items[0];
      gr_complex *out = (gr_complex*)output_items[0];


      const float *in_float = (const float*) input_items[0];



        // Do <+signal processing+>

      for(int i =0 ; i < noutput_items ; i++){
        out[i] = in[i];


      }

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace COWN */
} /* namespace gr */

