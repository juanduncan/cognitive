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
#include "sink_test_impl.h"

using namespace std;
namespace gr {
  namespace avio505 {

    sink_test::sptr
    sink_test::make()
    {
      return gnuradio::get_initial_sptr
        (new sink_test_impl());
    }

    /*
     * The private constructor
     */
    sink_test_impl::sink_test_impl()
      : gr::sync_block("sink_test",
              gr::io_signature::make(1, 1,  sizeof(gr_complex)),
              gr::io_signature::make(0, 0, 0)),
      total(0)
    {}

    /*
     * Our virtual destructor.
     */
    sink_test_impl::~sink_test_impl()
    {
    }

    int
    sink_test_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *in = (const gr_complex*) input_items[0];

        // Do <+signal processing+>
        total = total + noutput_items;
        cout << "noutput_items ="<< noutput_items*1.00 << " \ttotal= " << total*1.00 << "\ttime = " << total/4e6   <<  endl;
        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace avio505 */
} /* namespace gr */

