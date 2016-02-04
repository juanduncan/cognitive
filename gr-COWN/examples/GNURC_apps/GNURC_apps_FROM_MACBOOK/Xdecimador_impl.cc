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
#include "decimador_impl.h"

namespace gr {
  namespace DataConversion {

    decimador::sptr decimador::make(size_t itemsize, size_t nitems_per_block)
    {
      return gnuradio::get_initial_sptr(new decimador_impl(itemsize, nitems_per_block));
    }


    /*
     * The private constructor
     */
    decimador_impl::decimador_impl(size_t itemsize, size_t nitems_per_block)
      : gr::sync_decimator("decimador",
			   io_signature::make (1, 1, itemsize),
			   io_signature::make (1, 1, itemsize * nitems_per_block),
			   nitems_per_block)
    {}

    /*
     * Our virtual destructor.
     */
    //decimador_impl::~decimador_impl()
    //{
    //}


    int
    decimador_impl::work(int noutput_items,
				 gr_vector_const_void_star &input_items,
				 gr_vector_void_star &output_items)
    {
      size_t block_size = output_signature()->sizeof_stream_item (0);
      
      const char *in = (const char *) input_items[0];
      char *out = (char *) output_items[0];
      
      memcpy (out, in, noutput_items * block_size);
      
      return noutput_items;
    }
    /*  
    int
    decimador_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const <+ITYPE+> *in = (const <+ITYPE+> *) input_items[0];
        <+OTYPE+> *out = (<+OTYPE+> *) output_items[0];

        // Do <+signal processing+>

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }
    */




  } /* namespace DataConversion */
} /* namespace gr */

