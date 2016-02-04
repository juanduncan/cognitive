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
#include "tx_valve2_impl.h"


using namespace std;


namespace gr {
  namespace COWN {

    tx_valve2::sptr
    tx_valve2::make()
    {
      return gnuradio::get_initial_sptr
        (new tx_valve2_impl());
    }

    /*
     * The private constructor
     */
    tx_valve2_impl::tx_valve2_impl()
      : gr::sync_block("tx_valve2",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(1, 1, sizeof(gr_complex)))
    {}

    /*
     * Our virtual destructor.
     */
    tx_valve2_impl::~tx_valve2_impl()
    {
    }

    int
    tx_valve2_impl::work(int noutput_items, 
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *in = (const gr_complex *) input_items[0];
        gr_complex *out = (gr_complex *) output_items[0];


        uint64_t abs_start = nitems_read(0) ;
        uint64_t abs_end = nitems_read(0) + noutput_items ;
		get_tags_in_range(d_tags, 0, abs_start,abs_end);
		 if (d_tags.size()) {
			 std::sort(d_tags.begin(), d_tags.end(), gr::tag_t::offset_compare);
			 gr::tag_t el =  d_tags.front();
			 //cout << "dtags " << el.key << "   " << el.value   << "\t";
			 cout << "size " << d_tags.size()   << "\t";
			 cout << "offset " << el.offset   << "\t";
			 el = d_tags[2];
			 //pmt::pmt_t packet_length = el.value;
			 packet_length = pmt::to_long(el.value);
			 cout << "dtags " << el.key << "   " <<   packet_length  << "\t";
			 cout<<  "nitems_read(0)" << ": "<<  nitems_read(0)<< "\t\t"  ;
			 cout<<  "nitems_written(0)" << ": "<<  nitems_written(0)<< "\t"  ;
			 cout<<  "Time Written" << ": "<<  nitems_written(0)/5e5<< "\t"  ;
			 //cout<<  "Ratio" << ": "<<  nitems_read(0)/nitems_written(0)*1.00 << "\t"  ;
			 cout << "noutput_items: "  << noutput_items  << "\t";
			 cout << "noutput_items: "  << noutput_items  << endl;
		 }else{ 
			 cout << "\tsize " << d_tags.size()   << "\t";
			 cout << "\t\t";
			 cout << "dtags " << "llama packet_length" << "   " <<   packet_length  << "\t";
			 cout<<  "nitems_read(0)" << ": "<<  nitems_read(0)<< "\t\t"  ;
			 cout<<  "nitems_written(0)" << ": "<<  nitems_written(0)<< "\t"  ;
			 cout<<  "Time Written" << ": "<<  nitems_written(0)/5e5<< "\t"  ;
			 //cout<<  "Ratio" << ": "<<  nitems_read(0)/nitems_written(0)*1.00 << "\t"  ;
			 cout << "noutput_items: "  << noutput_items   << "\t";
			 cout << "noutput_items: "  << noutput_items  << endl;
	      }




		std::memset(out, 0x00, sizeof(gr_complex) * (   noutput_items + 400 ));


		memcpy(out, in,noutput_items*8 );
			
        return (noutput_items);
    }

  } /* namespace COWN */
} /* namespace gr */

